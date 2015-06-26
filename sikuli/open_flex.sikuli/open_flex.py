click("Createanewpr.png")
wait(1)
type( "hello")
click("OK.png")
if exists(Pattern("OK-2.png").similar(0.88)):
    click(Pattern("OK-1.png").similar(0.86))
else:
    click(Pattern("Qpen.png").similar(0.80))
    
