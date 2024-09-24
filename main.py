import streamlit as st
from datetime import datetime, timedelta

st.title("Insira os valores de TEMPO")

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
    years = st.number_input("Anos Gastos", min_value=min, max_value=max, value=value)
    if years > max:
        st.error(f"O número de anos informado é maior que o limite definido: {max}.")
    
    st.write(f"O número de anos informado foi: {years}")
    return years

if __name__ == "__main__":
    time_spent_before_work = _input_time("Informe o tempo gasto para se preparar de manhã:", "Formato (HH:MM:SS)")
    commute_time = _input_time("Informe o tempo de trajeto até o trabalho (Apenas IDA)", "Consideraremos a VOLTA com base no valor de IDA.")

    if time_spent_before_work and commute_time:
        
        # Soma dos tempos
        time_spent_in_a_day = time_spent_before_work + commute_time

        # Exibe o resultado
        st.write(f"Tempo total gasto no dia: {str(time_spent_in_a_day)}")

    year = _input_years()