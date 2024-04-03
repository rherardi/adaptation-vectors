# adaptation-vectors

Simple modeling tool to generate what if scenarios representing rate of change in technology versus ability of workers to adapt to change

## Links

- [Repo](https://github.com/rherardi/adaptation-vectors) GitHub Repo)

## Purpose

The purpose of the tool is to model potential displacements of workers due to technological changes affecting the workplace and job market.

Time is required for workers to re-skill or upskill in order to remain employable. The magnitude and complexity of technological change influence how long workers require to re-skill or upskill. The timespan over which technological change occurs can range from (1) long enough to reasonably expect virtually all workers to be able to adapt, to (2) too short to reasonably expect any worker to be able to adapt, i.e., to remain employable. In teh former case, workers might simply adopt new technologies or learn to use new technological tools. In the latter case, jobs might be abruptly replaced as a result of new technologies.

## Available Commands

In the project directory, you can run:

### `adaptation_vectors.py <p1> <p2>`

p1 = time (in months) available for workers to adapt
p2 = time (in months) required for workers to adapt

### Description

The tool distributes randomly generated points in a 3D field, divides points into five 20% tranches based on Y values, producing 5 tranches of workers, and draws a cross-cutting line (demarcating the top 20% of workers by default).

The position of the cross-cutting line relative to the array of points varies depending on input values representing time (in months) available for workers to adapt (p1) versus time required for workers to adapt (p2). Both time available and time required for workers to adapt are equal to 60 months by default.

Different input values result in greater or lesser proportions of the workforce falling above or below the line. The resulting scenarios (visualized as 3D graphs) represent the employability or unemployability of workers as a function of the timespan over which technology change occurs, which is a proxy for the rate of technological change.

## Built With

- Python
- numpy
- matplotlib

## Author

**Ron Herardian**

- [Profile](https://github.com/rherardi "Ron Herardian")
- [Email](mailto:ron@basilsecurity.com "Email")

## 🤝 Support

Contributions, issues, and feature requests are welcome!

Give a ⭐️ if you like this project!
