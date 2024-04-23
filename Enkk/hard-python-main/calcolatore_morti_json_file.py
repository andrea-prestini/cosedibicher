import json


with open("deadge.json") as f:
    data = json.load(f)

f_year = "2001"
f_month = "January"


def year_all_month_morti(s_year):
    for month in data[s_year].keys():
        morti_mese_value = 0
        for day, dod in data[s_year][month].items():
            morti_mese_value += len(dod)
        print("Anno", s_year, "Mese:", month, "morti:", morti_mese_value)


def year_month_morti(s_year, s_month):
    for year in data.keys():
        if year == s_year:
            for month in data[s_year].keys():
                if month == s_month:
                    morti_mese_value = 0
                    for day, dod in data[s_year][month].items():
                        morti_mese_value += len(dod)
    print("Anno:", s_year, "Mese:", s_month, "morti:", morti_mese_value)


def year_morti_totali():
    for year in data.keys():
        morti_anno_value = 0
        for month in data[year].keys():
            for day, dod in data[year][month].items():
                morti_anno_value += len(dod)
        print("Anno:", year, "morti:", morti_anno_value)


def year_montly_morti():
    for anno, anno_vals in data.items():
        for mese, mese_vals in anno_vals.items():
            morti_mese_value = 0
            for giorno, giorno_vals in mese_vals.items():
                morti_mese_value += len(giorno_vals)
            print(anno, mese, morti_mese_value)


def gran_total_deads():
    morti = 0
    for year in data.keys():
        for month in data[year].keys():
            for day, dod in data[year][month].items():
                morti += len(dod)
    print("morti:", morti)


# year_all_month_morti(f_year)
# year_month_morti(f_year, f_month)
# year_morti_totali()
# year_montly_morti()
# gran_total_deads()
