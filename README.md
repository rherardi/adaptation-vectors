# Adaptation Vectors

Simple modeling tool to generate what if scenarios representing rate of change in technology versus ability of workers to adapt to change

## Links

- [Repo](https://github.com/rherardi/adaptation-vectors "Adaptation Vectors GitHub")

## Purpose

The purpose of this tool is to model the impact of potentially disruptive technological changes affecting the labor market. Workers either adapt to and learn to use new technologies or are displaced.

* Time is required for workers to up-skill or re-skill in order to remain relevant in the labor market, i.e., to remain employable and ultimately to remain in the workforce.
* The magnitude and complexity of technological change influence how long workers require to up-skill or re-skill.
* The timespan over which technological change occurs can range from (1) long enough to reasonably expect virtually all workers to adapt, to (2) too short a time to reasonably expect any worker adapt.

## Available Commands

In the project directory, you can run:

```console
python adaptation_vectors.py <p1> <p2>
```

p1 = time (in months) in which disruptive technology change occurs (max time available for workers to adapt)
p2 = time (in months) needed for workers to adapt to technology change, i.e., to up-skill or re-skill

### Technical Description

The tool distributes randomly generated points in a 3D field, divides points into five 20% tranches based on Y values, producing 5 tranches of workers, and draws a cross-cutting line (demarcating the top 20% of workers by default).

The position of the cross-cutting line relative to the array of points varies depending on input values representing time (in months) available for workers to adapt (p1) versus time required for workers to adapt (p2). Both time available and time required for workers to adapt are equal to 60 months by default.

Different input values result in greater or lesser proportions of the workforce falling above or below the line. The resulting scenarios (visualized as 3D graphs) represent the employability or unemployability of workers as a function of the timespan over which technology change occurs, which is a proxy for the rate of technological change.

## Built With

- Python
- numpy
- matplotlib

# Running the Adaptation Vectors Jupyter Notebook
A Jupyter notebook, adaptation_vectors.ipynb, s included and contains the above Python program.

## Prerequisites
Python 3 installed on your system.
Jupyter Notebook installed (can be installed via pip: pip install notebook).

# Steps to Run the Notebook
Clone or download the repository containing the Jupyter notebook file (adaptation_vectors.ipynb).
Change directories to the directory where the notebook file is located then launch Jupyter Notebook

```console
jupyter notebook <adaptation_vectors.ipynp>
```

Once the notebook is open, run each cell by selecting it and pressing Shift + Enter. Alternatively, you can use the Run button from the toolbar. The notebook will provide fields for entering the total months and maximum months to adapt.

After executing all the cells, you will find a generated CSV file (adaptation_vectors.csv) containing the data and a PNG file (adaptation_vectors.png) containing the 3D graph in the same directory as the notebook.

## Author

**Ron Herardian**

- [Profile](https://github.com/rherardi "Ron Herardian")
- [Email](mailto:6821925+rherardi@users.noreply.github.com "Email")

## 🤝 Support

Contributions, issues, and feature requests are welcome!

Give a ⭐️ if you like this project!

