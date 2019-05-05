# Parkinglot (Image processing project)

Team students name:
- أحمد سيد أحمد محمد
&nbsp;
- عبدالله محسن سيد
&nbsp;
- منة ناصر عبدالتواب
&nbsp;
- مروة راوي عبدالحميد
&nbsp;
- عصمت سعيد خميس

---

Requirements & Installation
------
- Python 3.5+ - Please see `python_req.txt` to know python modules are required
&nbsp;
- XAMPP 3.1^ (PHP localhost) for running the app
you can download it from this link: [https://www.apachefriends.org/download.html](https://www.apachefriends.org/download.html)
&nbsp;
you can also see this tutorial: [https://www.youtube.com/watch?v=k9em7Ey00xQ](https://www.youtube.com/watch?v=k9em7Ey00xQ)
&nbsp;

---

Running
------
1. To run parking lot from root folder: `python main.py --mode 1` for mode 1 or `python main.py --mode 2` for mode 2
2. Detect the 4 corners of parking lot place then click `t` or for reset click `r`
3. Fore running `App` please make sure you setup `XAMPP` first then open `app.html`

---

Project description
------
Today’s technology development has speed up our life so that everything around us gets smarter, integrable, faster and sometimes more complex or easier depending on the goal to be achieved.

Nowadays, Image processing and computer vision involved in many real and daily life applications.
One of that applications which we will consider as our project is used to solve a daily issue exits in our life. The where to park in parking areas situation?

Every time you are looking to park your car you need to circle around to find out a free parking spot. That way of search is slow and frustrating. As, sometimes you aren’t the luckiest person ever and after spending time turning all around the parking area you won’t find a free space for parking as the whole parking is full of cars.

Hence, we concern in presenting an application that will be capable of providing you with information about the parking lot you are looking to park your car in.
  - If there is a free space for you or not?
  - where exactly that free spot in the parking lot to go direct to it saving your effort and time


---


Project Impact
------
> On individuals
-	Optimization for driver time, efforts and resources – e.g. car fuel.
<br/> Through finding the suitable parking spot in the nearest parking lot. So, you won't be late on your meeting and appointments anymore
> On community
-	Traffic jam reduction.
  <br/>As, the number of the cars circling around to find free parking spot ‘ll be reduced
> On Environment
-	The other plus side is the environmental impact.
  <br/>The less drivers idle, cruise and search for parking, the less the negative impact on the environment.
  <br/>As, the decrement in number of cars turning around will also decrease the amount of vehicle oil burnt and by turn reduces the global ecological footprint.

---

Algorithm Procedure
------
The implementation of the desired project through the main following points:
>1. DETERMINE THE PARKING SLOTS IN THE PARKING LOT

The configuration of the parking slots in an image or video frame can be achieved using:
  -	Edge detection using canny functions to get the benefits of white lines of the parking spots then Hough line to specifically determine the start and the end of the line in the image
  -	Then, followed by drawing contour for each parking spot and numbering the slots. So that, the numbers can be used further in the reset of the algorithm

But, the issue of the previously mentioned method is the following:
  -	Needs an image for the parking lot when it’s completely empty.
  -	If there are any obstacles in the camera view e.g.: tree – light column – etc. that will also add noise to the detection of existing parking slots either there ‘ll be slots won’t be detected or others will be detected as free when they are aren’t
  -	The contour drawing process almost will require a user input at the first time the algorithm run.

So, it’s better to use another way that will also depend on user input (meant to be the team responsible of setting the algorithm at the parking lot to operate)
  -	The method to be used is the formation of YAML file that contains the coordinates of the parking slots in the parking lot
>2. DETECT ANY EXISTING MOTION OR CHANGE IN THE PARKING LOT

That step can be implemented using background subtraction algorithms:
  - MOG algorithm
  - ROI (Region of Interest) algorithm

>3. ASSIGN THE FREE AND THE BUSY PARKING SLOTS

---

Note
------
Please keep in mind that the code was compiled at the beginning without the use `Github`
and as a team we finally compiled the code with each and everyone of us has thier
own mark `(at comments)` on the part they did in the project

---

License
------
MIT
