def generate_mermaid_diagram(json_data):
    """
    Генерирует код Mermaid для диаграммы последовательности (sequenceDiagram).
    """
        
    mermaid_lines = [
        "sequenceDiagram",
        "    autonumber",
        "    actor User as Пользователь (PM)"
    ]
    
    # Добавляем участников (агентов)
    for agent_id, agent_name in json_data["agents"].items():
        mermaid_lines.append(f"    participant {agent_id} as {agent_name}")
    
    mermaid_lines.append("")  # Пустая строка для разделения

    current_context = json_data["base_repo_tokens"]
    
    # Проход по шагам пайплайна
    for step in json_data["pipeline"]:
        sender = step["from"]
        receiver = step["to"]
        desc = step["desc"]
        out_tokens = step["out"]
        is_error = step.get("is_error", False)
        
        # Добавляем технические заметки для не-User отправителей
        if sender != "User":
            mermaid_lines.append(f"    note over {sender}: [In: {current_context / 1000:.1f}k] -> {desc}")
        
        # Определяем стрелку
        arrow = "-->>" if is_error or receiver == "User" else "->>"
        
        # Формируем строку с описанием и выходом
        if out_tokens > 0:
            mermaid_lines.append(f"    {sender}{arrow}{receiver}: {desc} [Out: {out_tokens / 1000:.1f}k]")
        else:
            mermaid_lines.append(f"    {sender}{arrow}{receiver}: {desc}")

        current_context += out_tokens
    
    return "\n".join(mermaid_lines)
