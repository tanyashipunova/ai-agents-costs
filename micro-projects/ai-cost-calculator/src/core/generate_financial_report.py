def generate_financial_report(json_data, price_in=3.00, price_out=15.00):
    """
    Генерирует только плановый финансовый отчет затрат по пайплайну.
    Тарифы указаны за 1 000 000 (1М) токенов.
    """
    current_context = json_data["base_repo_tokens"]
    total_in_tokens = 0
    total_out_tokens = 0
    
    table_header = (
        f"{'Отправитель':<20} | {'Действие / Описание':<30} | "
        f"{'Вход (In)':<10} | {'Выход (Out)':<12} | "
        f"{'Стоимость ($)':<12}"
    )
    table_rows = [table_header, "-" * 93]
    
    for step in json_data["pipeline"]:
        sender = step["from"]
        receiver = step["to"]
        desc = step["desc"]
        out_tokens = step["out"]
        
        # Формирование входа в токенах (в k-формате)
        in_k = f"{current_context / 1000:.1f}k"
        out_k = f"{out_tokens / 1000:.1f}k" if out_tokens > 0 else "0"
        
        # Финансовая часть
        step_in = current_context
        cost_in = (step_in / 1_000_000) * price_in
        cost_out = (out_tokens / 1_000_000) * price_out
        step_total_cost = cost_in + cost_out
        
        total_in_tokens += step_in
        total_out_tokens += out_tokens
        
        agent_clean_name = json_data["agents"].get(sender, "User")
        table_rows.append(
            f"{agent_clean_name:<20} | {desc:<30} | "
            f"{step_in:<10,} | {out_tokens:<12,} | ${step_total_cost:.4f}"
        )
        
        current_context += out_tokens
    
    # Финальные итоги
    total_cost_in = (total_in_tokens / 1_000_000) * price_in
    total_cost_out = (total_out_tokens / 1_000_000) * price_out
    grand_total = total_cost_in + total_cost_out
    
    table_rows.append("-" * 93)
    table_rows.append(f"ОБЩИЙ БЮДЖЕТ ЦИКЛА:")
    table_rows.append(f"Всего входных токенов: {total_in_tokens:,} (Затраты: ${total_cost_in:.4f})")
    table_rows.append(f"Всего выходных токенов: {total_out_tokens:,} (Затраты: ${total_cost_out:.4f})")
    table_rows.append(f"Финальная стоимость выполнения задачи: ${grand_total:.4f}")
    
    return "\n".join(table_rows)

