time = "24.02.2020"

print(list)
def get_month_name(number):
    if number == 1:
        month_name = "Jaanuar"
    if number == 2:
        month_name = "Veebruar"
    if number == 3:
        month_name = "Märts"
    if number == 4:
        month_name = "Aprill"
    if number == 5:
        month_name = "Mai"
    if number == 6:
        month_name = "Juuni"
    if number == 7:
        month_name = "Juuli"
    if number == 8:
        month_name = "August"
    if number == 9:
        month_name = "September"
    if number == 10:
        month_name = "Oktoober"
    if number == 11:
        month_name = "November"
    if number == 12:
        month_name = "Detsember"
    return month_name
def time_convert_to_formatted(time):
    list = time.split(".")
    month = get_month_name(int(list[1]))
    finished_format = f"{list[0]}. {month} {list[2]}. a"
    return finished_format


time = input("Sisesta kuupäev kujul DD.MM.YYYY: ")
print(time_convert_to_formatted(time))