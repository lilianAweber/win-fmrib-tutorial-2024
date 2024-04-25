from psychopy import visual, core, event

stim1 = visual.TextStim(t='Stimulus 1', pos=(0, 0), color='black')
stim2 = visual.TextStim(t='Stimulus 2', pos=(0, 0), color='black')

win = visual.Window(size=(800, 600), color='white', units='pix')

wtext = visual.TextStim(win, text='Welcome!', pos=(0, 50), color='black')
wtext.draw()
win.flip()
core.wait(2)

for t in range(60):
    stim1.draw()
    win.flip()
    core.wait(0.5)

    stim2.draw()
    win.flip()
    core.wait(0.5)

    keys = event.waitKeys(keyList=['1', '2'])
    res = keys[0]

    print(f'Trial {t+1}: Participant responded with {res}')

ctext = visual.TextStim(win, text='Task done!', pos=(0, 50), color='black')
ctext.draw()
win.flip()
core.wait(2)

win.close()

# WIN
