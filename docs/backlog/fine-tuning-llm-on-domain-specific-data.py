# Пример реализации на Python

from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
from peft import LoraConfig, get_peft_model
import torch
from accelerate import Accelerator

# 1. Загружаем модель и токенизатор
model_name = "tiny-llm"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# 2. Настройка LoRA
lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["q_proj", "v_proj"],  # модули, где применять LoRA
    lora_dropout=0.1,
    bias="none",
    task_type="CAUSAL_LM"
)

# Применяем LoRA
model = get_peft_model(model, lora_config)

# 3. Настройка обучения
training_args = TrainingArguments(
    output_dir="./lora_finance_model",
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,
    num_train_epochs=3,
    learning_rate=2e-5,
    logging_dir="./logs",
    logging_steps=10,
    save_steps=500,
    fp16=True,  # используем FP16 для экономии памяти
    gradient_checkpointing=True,  # включаем gradient checkpointing
    optim="adamw_torch",
    report_to="tensorboard",
)

#  4. Загружаем датасет (например, JSON-файлы с маркетинговыми отчётами)
from datasets import load_dataset
dataset = load_dataset("json", data_files="marketing_reports.json")

# 5. Подготовка данных (токенизация)
def tokenize_function(examples):
    return tokenizer(examples["text"], truncation=True, padding="max_length", max_length=512)

dataset = dataset.map(tokenize_function, batched=True)

# 6. Обучение
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    tokenizer=tokenizer,
)

trainer.train()

# 7. Сохранение модели
model.save_pretrained("./finetuned_finance_llm")
tokenizer.save_pretrained("./finetuned_finance_llm")
