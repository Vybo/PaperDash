# PaperDash
My own dashboard implemented for Waveshare 7.5" BTW e-paper display

## Currently supported features
0. Main loop scheduled to run every minute at the 0 seconds mark (adjusted -10 seconds if using e-paper display with slow update so the on-screen information is not delayed)
1. Rendering
  * Rendering to Tkinker window canvas for debugging purposes
  * EBD library working with Waveshare 7.5" BTW V1
2. UI Parts
  * Fullscreen text message
  * Fullscreen text message with icon (loaded from file)
3. Dashboards (somewhat self-sufficient ViewModels handling what to draw into UI Parts)
  * Fulscreen clock
  
## Planned features
* Cycling of various Dashboards
* Widgetized dashboards (splitting into smaller ViewModels)
* Various data sources for ViewModels (will need some multithreading work)
* More UI parts

![Rendering to e-paper display][ebd-render]
![Rendering to Tkinker window][window-render]

[ebd-render]: https://github.com/Vybo/PaperDash/blob/master/Readme/ebd-render.png "Rendering to e-paper display"
[window-render]: https://github.com/Vybo/PaperDash/blob/master/Readme/window-render.png "Rendering to Tkinker window"
