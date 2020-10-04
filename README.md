# Loxberry_Power_Button
Dieses Plugin stellt die Funktionen eines Powerbuttons an Pin 5 (GPIO-3) eines Raspberry PI bereit. Zudem kann über Pin 7 (GPIO-4) eine Rückmelde-LED angeschlossen werden.
Der Powerbutton muss hierfür ein Taster sein, welcher mittels eines PullUp-Widerstandes von 10kOhm an Pin 5 angeschlossen wird. Die LED muss mittels Vorwiderstand zwischen Pin7 und GND angeschlossen werden.
Folgende Funktionen sind implementiert:
Betätigung des Buttons < 2.5 Sekunden: 
Loxberry Runterfahren, LED blinkt zur Bestätigung 3 mal mit 1 Hz
Betätigung des Buttons > 2.5 Sekunden: 
Loxberry Neu starten, LED blinkt zur Bestätigung 5 mal mit 3 Hz
Viel Spaß!
