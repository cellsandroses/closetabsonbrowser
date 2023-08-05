# closetabsonbrowser
python script to close tabs open in browser
1-Install pyautogui library by running pip install pyautogui

Here I use the pyautogui library to simulate pressing Ctrl + W which works to close tabs in a lot of browsers. Before running the script, you need to be in the web browser that has the tabs you want to close because it starts closing tabs after a 5-second delay. The close_tabs function takes the num_tabs_to_close parameter, which specifies the number of tabs you want to close; this value can be changed and customized as needed. There is also a delay of 0.5 seconds between closing each tab so that the browser can have time to process the command before moving onto the next tab.

Be careful with this script because it can close unsaved work and important apps which are open; the browser needs to be the active window for it to work properly and not close work.
 
