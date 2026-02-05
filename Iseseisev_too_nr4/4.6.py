
print(list)
months = ["Jaanuar", "Veebruar", "Märts", "Aprill", "Mai", "Juuni", "Juuli", "August", "September", "Oktoober", "November", "Detsember"]
def get_month_name(number):
    month_name = months[number-1]
    return month_name
def time_convert_to_formatted(time):
    list = time.split(".")
    month = get_month_name(int(list[1]))
    finished_format = f"{list[0]}. {month} {list[2]}. a"
    return finished_format


time = input("Sisesta kuupäev kujul DD.MM.YYYY: ")
print(time_convert_to_formatted(time))