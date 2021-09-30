# Particles 🔥
<br>

Although I used Pygame, the main concept can be used with any library (it doesn't matter which language you use)
<br><b>Read <a href="https://natureofcode.com/book/chapter-4-particle-systems/#:~:text=We've%20defined%20a%20particle,a%20simple%20shape%20or%20dot.&text=If%20we%20want%20to%20get,with%20systems%20of%20many%20things.">this</a> btw.</b>

![Demo](https://raw.githubusercontent.com/Datavorous/particles/main/media/Untitled%2028_720p.gif)
<br>
## Example
Take a look below ↓
<br>
```python
myParticles = Particles(
    screen=screen,
    surface=r"res/orange.png",
    pos_x=0,
    pos_y=0,
    lifetime=3,
    direction_x=2,
    direction_y=2)
```
You can tweak with this parameters to create some interesting effects!<br>
```opacity``` is included inside the ```Particles``` class and is randomised from 0 to 255


