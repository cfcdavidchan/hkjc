from pprint import pprint

from helper import helper # imporrt helper function
cred_json = 'HKJC-google-cred.json'
worksheet_key = '1jrD0x3qlBVELqyqMUDrIIHj0h66RYIlx48JELNd8ERQ'
from string import ascii_uppercase
import csv

def google_jockey_data(google, sheet_index):
    result = helper.get_list_jockey_season_report()

    data = []

    header = ['騎師', '負榜優勢',
              '今季出賽', '冠', '亞', '季', '殿', '今季分數',
              '上季出賽', '冠', '亞', '季', '殿', '上季分數','綜合分數']

    data.append(header)

    for i in range(len(result)):
        row = []
        row_number = i+2
        jockey_data = result[i]
        row.append(jockey_data[0])  # jockey name

        current_equation = "=IF(C{0}>'設定'!$D$12,(D{0}/C{0}*'設定'!$E$2+E{0}/C{0}*'設定'!$E$3+F{0}/C{0}*'設定'!$E$4+G{0}/C{0}*'設定'!$E$5)*'設定'!$E$12,IF(C{0}>'設定'!$D$13,(D{0}/C{0}*'設定'!$E$2+E{0}/C{0}*'設定'!$E$3+F{0}/C{0}*'設定'!$E$4+G{0}/C{0}*'設定'!$E$5)*'設定'!$E$13,IF(C{0}>'設定'!$D$14,(D{0}/C{0}*'設定'!$E$2+E{0}/C{0}*'設定'!$E$3+F{0}/C{0}*'設定'!$E$4+G{0}/C{0}*'設定'!$E$5)*'設定'!$E$14,IF(C{0}>'設定'!$D$15,(D{0}/C{0}*'設定'!$E$2+E{0}/C{0}*'設定'!$E$3+F{0}/C{0}*'設定'!$E$4+G{0}/C{0}*'設定'!$E$5)*'設定'!$E$15,IF(C{0}>'設定'!$D$16,(D{0}/C{0}*'設定'!$E$2+E{0}/C{0}*'設定'!$E$3+F{0}/C{0}*'設定'!$E$4+G{0}/C{0}*'設定'!$E$5)*'設定'!$E$16,(D{0}/C{0}*'設定'!$E$2+E{0}/C{0}*'設定'!$E$3+F{0}/C{0}*'設定'!$E$4+G{0}/C{0}*'設定'!$E$5)*'設定'!$E$17)))))".format(row_number)
        previous_equation = "=IF(I{0}=0,0,IF(I{0}>'設定'!$D$12,(J{0}/I{0}*'設定'!$E$2+K{0}/I{0}*'設定'!$E$3+L{0}/I{0}*'設定'!$E$4+M{0}/I{0}*'設定'!$E$5)*'設定'!$E$12,IF(I{0}>'設定'!$D$13,(J{0}/I{0}*'設定'!$E$2+K{0}/I{0}*'設定'!$E$3+L{0}/I{0}*'設定'!$E$4+M{0}/I{0}*'設定'!$E$5)*'設定'!$E$13,IF(I{0}>'設定'!$D$14,(J{0}/I{0}*'設定'!$E$2+K{0}/I{0}*'設定'!$E$3+L{0}/I{0}*'設定'!$E$4+M{0}/I{0}*'設定'!$E$5)*'設定'!$E$14,IF(I2>'設定'!$D$15,(J{0}/I{0}*'設定'!$E$2+K{0}/I{0}*'設定'!$E$3+L{0}/I{0}*'設定'!$E$4+M{0}/I{0}*'設定'!$E$5)*'設定'!$E$15,IF(I{0}>'設定'!$D$16,(J{0}/I{0}*'設定'!$E$2+K{0}/I{0}*'設定'!$E$3+L{0}/I{0}*'設定'!$E$4+M{0}/I{0}*'設定'!$E$5)*'設定'!$E$16,(J{0}/I{0}*'設定'!$E$2+K{0}/I{0}*'設定'!$E$3+L{0}/I{0}*'設定'!$E$4+M{0}/I{0}*'設定'!$E$5)*'設定'!$E$17))))))".format(row_number)
        for current_data in jockey_data[1]['current season']:
            row.append(current_data)
        row.append(current_equation)
        for previous_data in jockey_data[1]['previos season']:
            row.append(previous_data)
        row.append(previous_equation)
        integrated_equation = "=H{0}*100*'設定'!$E$8+N{0}*100*'設定'!$E$9+B{0}".format(row_number)
        row.append(integrated_equation)
        data.append(row)

    google.clean_and_write(sheet_index= sheet_index, data=data)
    google.get_worksheet(sheet_index).format("H:H", {"horizontalAlignment": "CENTER",
                                                           'numberFormat': {
                                                               "type": "PERCENT",
                                                               "pattern": '.##%'},
                                                           "textFormat": {
                                                               "foregroundColor": {"red": 0.0,
                                                                                   "green": 0.0,
                                                                                   "blue": 2.0
                                                                                   }
                                                           }
                                                           })

    google.get_worksheet(sheet_index).format("N:N", {"horizontalAlignment": "CENTER",
                                                           'numberFormat': {
                                                               "type": "PERCENT",
                                                               "pattern": '.##%'},
                                                           "textFormat": {
                                                               "foregroundColor": {"red": 0.0,
                                                                                   "green": 0.0,
                                                                                   "blue": 2.0
                                                                                   }
                                                           }
                                                           })

    google.get_worksheet(sheet_index).format("O:O", {"horizontalAlignment": "CENTER",
                                                           "textFormat": {
                                                               "foregroundColor": {"red": 0.0,
                                                                                   "green": 0.0,
                                                                                   "blue": 2.0
                                                                                   }
                                                           }
                                                           })
    print ('Success to store Jockey Data store into Google')

def google_trainer_data(google, sheet_index):
    trainer_dict = helper.get_list_trainer_season_report()
    # Sha Tin turf current season mark, last season mark, integrated mark
    # 沙田草地今季分數, 沙田草地上季分數, 總分
    ST_turf_current_formula= "=IF(B{0}>'設定'!$G$12,(C{0}/B{0}*'設定'!$H$2+D{0}/B{0}*'設定'!$H$3+E{0}/B{0}*'設定'!$H$4+F{0}/B{0}*'設定'!$H$5)*'設定'!$H$12,IF(B{0}>'設定'!$G$13,(C{0}/B{0}*'設定'!$H$2+D{0}/B{0}*'設定'!$H$3+E{0}/B{0}*'設定'!$H$4+F{0}/B{0}*'設定'!$H$5)*'設定'!$H$13,IF(B{0}>'設定'!$G$14,(C{0}/B{0}*'設定'!$H$2+D{0}/B{0}*'設定'!$H$3+E{0}/B{0}*'設定'!$H$4+F{0}/B{0}*'設定'!$H$5)*'設定'!$H$14,(C{0}/B{0}*'設定'!$H$2+D{0}/B{0}*'設定'!$H$3+E{0}/B{0}*'設定'!$H$4+F{0}/B{0}*'設定'!$H$5)*'設定'!$H$15)))"
    ST_turf_last_formula = "=IF(H{0}=0,0,IF(H{0}>'設定'!$G$12,(I{0}/H{0}*'設定'!$H$2+J{0}/H{0}*'設定'!$H$3+K{0}/H{0}*'設定'!$H$4+L{0}/H{0}*'設定'!$H$5)*'設定'!$H$12,IF(H{0}>'設定'!$G$13,(I{0}/H{0}*'設定'!$H$2+J{0}/H{0}*'設定'!$H$3+K{0}/H{0}*'設定'!$H$4+L{0}/H{0}*'設定'!$H$5)*'設定'!$H$13,IF(H{0}>'設定'!$G$14,(I{0}/H{0}*'設定'!$H$2+J{0}/H{0}*'設定'!$H$3+K{0}/H{0}*'設定'!$H$4+L{0}/H{0}*'設定'!$H$5)*'設定'!$H$14,(I{0}/H{0}*'設定'!$H$2+J{0}/H{0}*'設定'!$H$3+K{0}/H{0}*'設定'!$H$4+L{0}/H{0}*'設定'!$H$5)*'設定'!$H$15))))"
    ST_turf_all_formula = "=G{0}*'設定'!$H$8*100+M{0}*'設定'!$H$9*100"

    # Sha Tin All Weather current season mark, last season mark, integrated mark
    ST_AllWeather_current_formula = "=IF(O{0}>'設定'!$G$18,(P{0}/O{0}*'設定'!$H$2+Q{0}/O{0}*'設定'!$H$3+R{0}/O{0}*'設定'!$H$4+S{0}/O{0}*'設定'!$H$5)*'設定'!$H$18,IF(O{0}>'設定'!$G$19,(P{0}/O{0}*'設定'!$H$2+Q{0}/O{0}*'設定'!$H$3+R{0}/O{0}*'設定'!$H$4+S{0}/O{0}*'設定'!$H$5)*'設定'!$H$19,IF(O{0}>'設定'!$G$20,(P{0}/O{0}*'設定'!$H$2+Q{0}/O{0}*'設定'!$H$3+R{0}/O{0}*'設定'!$H$4+S{0}/O{0}*'設定'!$H$5)*'設定'!$H$20,(P{0}/O{0}*'設定'!$H$2+Q{0}/O{0}*'設定'!$H$3+R{0}/O{0}*'設定'!$H$4+S{0}/O{0}*'設定'!$H$5)*'設定'!$H$21)))"
    ST_AllWeather_last_formula = "=IF(U{0}=0,0,IF(U{0}>'設定'!$G$18,(V{0}/U{0}*'設定'!$H$2+W{0}/U{0}*'設定'!$H$3+X{0}/U{0}*'設定'!$H$4+Y{0}/U{0}*'設定'!$H$5)*'設定'!$H$18,IF(U{0}>'設定'!$G$19,(V{0}/U{0}*'設定'!$H$2+W{0}/U{0}*'設定'!$H$3+X{0}/U{0}*'設定'!$H$4+Y{0}/U{0}*'設定'!$H$5)*'設定'!$H$19,IF(U{0}>'設定'!$G$20,(V{0}/U{0}*'設定'!$H$2+W{0}/U{0}*'設定'!$H$3+X{0}/U{0}*'設定'!$H$4+Y{0}/U{0}*'設定'!$H$5)*'設定'!$H$20,(V{0}/U{0}*'設定'!$H$2+W{0}/U{0}*'設定'!$H$3+X{0}/U{0}*'設定'!$H$4+Y{0}/U{0}*'設定'!$H$5)*'設定'!$H$21))))"
    ST_AllWeather_all_formula  = "=T{0}*'設定'!$H$8*100+ z{0}*'設定'!$H$9*100"

    # Happy Valley turf current season mark, last season mark, integrated mark
    HV_turf_current_formula = "=IF(AB{0}>'設定'!$G$24,(AC{0}/AB{0}*'設定'!$H$2+AD{0}/AB{0}*'設定'!$H$3+AE{0}/AB{0}*'設定'!$H$4+AF{0}/AB{0}*'設定'!$H$5)*'設定'!$H$24,IF(AB{0}>'設定'!$G$25,(AC{0}/AB{0}*'設定'!$H$2+AD{0}/AB{0}*'設定'!$H$3+AE{0}/AB{0}*'設定'!$H$4+AF{0}/AB{0}*'設定'!$H$5)*'設定'!$H$25,IF(AB{0}>'設定'!$G$26,(AC{0}/AB{0}*'設定'!$H$2+AD{0}/AB{0}*'設定'!$H$3+AE{0}/AB{0}*'設定'!$H$4+AF{0}/AB{0}*'設定'!$H$5)*'設定'!$H$26,(AC{0}/AB{0}*'設定'!$H$2+AD{0}/AB{0}*'設定'!$H$3+AE{0}/AB{0}*'設定'!$H$4+AF{0}/AB{0}*'設定'!$H$5)*'設定'!$H$27)))"
    HV_turf_last_formula = "=IF(AH{0}=0,0,IF(AH{0}>'設定'!$G$24,(AI{0}/AH{0}*'設定'!$H$2+AJ{0}/AH{0}*'設定'!$H$3+AK{0}/AH{0}*'設定'!$H$4+AL{0}/AH{0}*'設定'!$H$5)*'設定'!$H$24,IF(AH{0}>'設定'!$G$25,(AI{0}/AH{0}*'設定'!$H$2+AJ{0}/AH{0}*'設定'!$H$3+AK{0}/AH{0}*'設定'!$H$4+AL{0}/AH{0}*'設定'!$H$5)*'設定'!$H$25,IF(AH{0}>'設定'!$G$26,(AI{0}/AH{0}*'設定'!$H$2+AJ{0}/AH{0}*'設定'!$H$3+AK{0}/AH{0}*'設定'!$H$4+AL{0}/AH{0}*'設定'!$H$5)*'設定'!$H$26,(AI{0}/AH{0}*'設定'!$H$2+AJ{0}/AH{0}*'設定'!$H$3+AK{0}/AH{0}*'設定'!$H$4+AL{0}/AH{0}*'設定'!$H$5)*'設定'!$H$27))))"
    HV_turf_all_formula = "=AG{0}*'設定'!$H$8*100+AM{0}*'設定'!$H$9*100"

    write_data = []
    header = ['練馬師',
              '今季田草出賽', '冠', '亞', '季', '殿', '今季田草分數',
              '上季田草出賽', '冠', '亞', '季', '殿', '上季田草分數',
              '田草分數',
              '今季田泥出賽', '冠', '亞', '季', '殿', '今季田泥分數',
              '上季田泥出賽', '冠', '亞', '季', '殿', '上季田泥分數',
              '田泥分數',
              '今季谷草出賽', '冠', '亞', '季', '殿', '今季谷草分數',
              '上季谷草出賽', '冠', '亞', '季', '殿', '上季谷草分數',
              '谷草分數',
              ]
    write_data.append(header)

    row_pointer = 2 #marking the row
    for trainer, result in trainer_dict.items():
        row = [trainer] # trainer name will be the first column of the row
        # Sha Tin turf
        for performance in result['沙田草地']['current season']:
            row.append(int(performance))
        row.append(ST_turf_current_formula.format(row_pointer)) # current season mark
        for performance in result['沙田草地']['previous season']:
            row.append(int(performance))
        row.append(ST_turf_last_formula.format(row_pointer)) # last season mark
        row.append(ST_turf_all_formula.format(row_pointer))  # integrated mark

        # Sha Tin All Weather
        for performance in result['沙田全天侯']['current season']:
            row.append(int(performance))
        row.append(ST_AllWeather_current_formula.format(row_pointer)) # current season mark
        for performance in result['沙田全天侯']['previous season']:
            row.append(int(performance))
        row.append(ST_AllWeather_last_formula.format(row_pointer)) # last season mark
        row.append(ST_AllWeather_all_formula.format(row_pointer))  # integrated mark

        # Happy Valley turf
        for performance in result['跑馬地草地']['current season']:
            row.append(int(performance))
        row.append(HV_turf_current_formula.format(row_pointer)) # current season mark
        for performance in result['跑馬地草地']['previous season']:
            row.append(int(performance))
        row.append(HV_turf_last_formula.format(row_pointer)) # last season mark
        row.append(HV_turf_all_formula.format(row_pointer))  # integrated mark

        write_data.append(row) # inert row to the write data

        row_pointer+= 1 #rolling to next row

    google.clean_and_write(sheet_index=sheet_index, data=write_data)

    # To Percent Format
    for range in ["G:G", "M:M", "T:T", "Z:Z", "AG:AG", "AM"]:
        google.get_worksheet(sheet_index).format(range, {"horizontalAlignment": "CENTER",
                                                         'numberFormat': {
                                                             "type": "PERCENT",
                                                             "pattern": '.##%'},
                                                         "textFormat": {
                                                             "foregroundColor": {"red": 0.0,
                                                                                 "green": 0.0,
                                                                                 "blue": 2.0
                                                                                 }
                                                         }
                                                         })

    # To Marks Format
    for range in ["N:N", "AA:AA", 'AN:AN']:
        google.get_worksheet(sheet_index).format(range, {"horizontalAlignment": "CENTER",
                                                         'numberFormat': {
                                                             "type": "NUMBER",
                                                             "pattern": '##.##'},
                                                         "textFormat": {
                                                             "foregroundColor": {"red": 0.0,
                                                                                 "green": 0.0,
                                                                                 "blue": 2.0
                                                                                 }
                                                         }
                                                         })

    print('Success to store Trainer Data store into Google')


def google_trainerXjockey(google, sheet_index, rate_type='in place'):
    trainerXjockey, all_trainer_chi_name, all_jockey_chi_name = helper.get_trainerXjockey_rate()

    write_data = []

    first_row = ['']
    for trainer in all_trainer_chi_name:
        first_row.append(trainer)
    write_data.append(first_row)

    for jockey in all_jockey_chi_name:
        row = [jockey]
        for trainer in all_trainer_chi_name:
            rate = trainerXjockey[trainer][jockey][rate_type][1]
            row.append(rate)

        write_data.append(row)

    google.clean_and_write(sheet_index=sheet_index, data=write_data)
    google.get_worksheet(sheet_index).format("B2:60", {"horizontalAlignment": "CENTER",
                                                     'numberFormat': {
                                                         "type": "PERCENT",
                                                         "pattern": '.##%'},
                                                     "textFormat": {
                                                         "foregroundColor": {"red": 0.0,
                                                                             "green": 0.0,
                                                                             "blue": 2.0
                                                                             }
                                                     }
                                                     })



google = helper.google_sheet_manager(cred_json, worksheet_key)
all_sheet = google.all_sheet_name_dict()
google_jockey_data(google, sheet_index= all_sheet['騎師資料'])
google_trainer_data(google, sheet_index= all_sheet['練馬師資料'])
google_trainerXjockey(google, sheet_index= all_sheet['練騎合拍_win'], rate_type= "in win")
google_trainerXjockey(google, sheet_index= all_sheet['練騎合拍_place'], rate_type= "in place")
# format the related shell


#print (all_sheet['騎師資料'])
# pprint (result)
# result = helper.get_list_jockey_season_report()
# first_row = result[1]
# name = first_row[0]
# current = first_row[1]['current season']
# print (name)
# print (current)

