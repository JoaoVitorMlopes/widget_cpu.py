import PySimpleGUI as sg
import psutil

sg.theme('black')

layout = [
    [sg.Text('', size=(8, 2), font=('Helvetica', 20), justification='center', key='text')],
    [sg.Exit(button_color=('white', 'firebrick4'), pad=((15,0), 0)), sg.Spin([x + 1 for x in range(10)], 1, key='spin')]
]

window = sg.Window('running timer', layout, no_titlebar=True, auto_size_buttons=False, keep_on_top=True, grab_anywhere=True)

while True:
    event, values = window.read(timeout=0)
    if event == sg.WIN_CLOSED or event == 'Exite':
        break
    try:
        inteval = int(values['spin'])
    except:
        inteval = 1
    cpu_percent = psutil.cpu_percent(interval=inteval)
    window['text'].update(f'cpu {cpu_percent:02.0f}%')

window.close()
