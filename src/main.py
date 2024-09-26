import streamlit as st
from datetime import datetime, timedelta

st.title("Calculadora de Tempo Perdido com Deslocamento ao Trabalho")

def _input_time(label_text, help_text):
    time_input = st.text_input(label_text, "00:00:00", help=help_text)

    try:
        hours, minutes, seconds = map(int, time_input.split(':'))
        st.write(f"O valor informado foi: {hours} horas, {minutes} minutos, e {seconds} segundos.")
    except ValueError:
        st.error("Por favor, insira o valor de tempo no seguinte formato HH:MM:SS.")
        return None
    
    time = datetime.strptime(time_input, "%H:%M:%S").time()
    time_dt = timedelta(hours=time.hour, minutes=time.minute, seconds=time.second)

    return time_dt

def _input_years(value: int = 1, min: int = 1, max: int = 62) -> int:
    years = st.number_input("Anos de trabalho", min_value=min, max_value=max, value=value)
    st.write(f"O número de anos informado foi: {years}")
    return years

def _input_work_days():
    days_per_year = st.number_input("Dias úteis por ano (média)", min_value=1, max_value=365, value=220)
    st.write(f"Dias úteis informados: {days_per_year}")
    return days_per_year

if __name__ == "__main__":
    time_spent_before_work = _input_time("Informe o tempo gasto para se preparar de manhã:", "Formato (HH:MM:SS)")
    commute_time = _input_time("Informe o tempo de trajeto até o trabalho (Apenas IDA)", "Consideraremos a VOLTA com base no valor de IDA.")
    
    if time_spent_before_work and commute_time:
        
        # Soma dos tempos (ida + volta)
        time_spent_in_a_day = time_spent_before_work + (commute_time * 2)
        st.write(f"Tempo total gasto no dia: {str(time_spent_in_a_day)}")
        
        years = _input_years() # Pergunta sobre os anos
        work_days_per_year = _input_work_days() # Pergunta sobre dias trabalhados em média por ano

        if st.button("Calcular"):

            # Calcula o tempo total perdido ao longo dos anos
            total_time_per_year = time_spent_in_a_day * work_days_per_year
            total_time_lost = total_time_per_year * years
            
            # resultado em dias
            total_days_lost = total_time_lost.total_seconds() / (60 * 60 * 24)
            st.write(f"Tempo total perdido ao longo de {years} anos: {int(total_days_lost)} dias.")
            
            if total_days_lost:
                st.balloons()
            
            years_complete = int(total_days_lost // 220)  # Parte inteira: anos completos 365 | Média de úteis por ano 220
            remaining_days = int(total_days_lost % 220)   # Resto: dias restantes

            # resultado final de anos e dias
            st.write(f"Equivalente a {years_complete} anos e {remaining_days} dias perdidos.")
