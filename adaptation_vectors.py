"""Simple modeling tool to generate 3D graphs representing worker re-skill / up-skill time versus available time, e.g., due to disruptive technological change."""

import argparse
import numpy as np
import matplotlib.pyplot as plt

def generate_data():
    # Generate 2500 points in a 3D field conforming to a gaussian distribution
    np.random.seed(0)
    x = np.random.normal(loc=50, scale=20, size=2500)
    y = np.random.normal(loc=50, scale=20, size=2500)
    z = np.random.normal(loc=50, scale=20, size=2500)
    return x, y, z

def save_csv(x, y, z):
    # Save points in a local CSV file
    data = np.column_stack((x, y, z))
    np.savetxt("adaptation_vectors.csv", data, delimiter=",", header="x,y,z", comments='', fmt='%0.2f')

def create_chart(x, y, z, t1, t2, t3, t4, t5, p1):
    # Chart points delineated by y axis value ("percent of workforce") color coding each 20% tier
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(111, projection='3d')

    # Define colors based on y values
    colors = np.where(y > y2, 'green',  # Green
                      np.where(y > y3, 'blue',  # Lightblue
                               np.where(y > y4, 'violet',  # Orange
                                        np.where(y > y5, 'purple',  # Orangered
                                                 'red'))))  # Red

    ax.scatter(x, y, z, c=colors)

    # Set y value demarcation at y2 (between top 20% and bottom 80% of y values) as a whole integer
    l4 = int(round(y2))

    # Draw demarcation line on chart
    ax.plot([100, 0], [l4, l4], [0, 100], color='black')

    # Set chart axis increments and labels
    ax.set_xticks(np.arange(0, 101, 10))
    ax.set_xticklabels(["{}%".format(i) for i in range(0, 101, 10)], fontsize=6)
    ax.set_xlabel("x = Time Available", fontsize=9)

    ax.set_yticks(np.arange(0, 101, 10))
    ax.set_yticklabels(["{}%".format(i) for i in range(0, 101, 10)], fontsize=6)
    ax.set_ylabel("y = Percent of Workforce", fontsize=9)

    ax.set_zticks(np.arange(0, 101, 10))
    ax.set_zticklabels(["{}%".format(i) for i in range(0, 101, 10)], fontsize=6)
    ax.set_zlabel("z = Ability to Adapt", fontsize=9)

    plt.savefig("adaptation_vectors.png")
    plt.close()

if __name__ == "__main__":
    # Parse commandline and emit messages on error, set default values if no input is provided
    parser = argparse.ArgumentParser(description="adaptation_vectors.py <total months> <max months to adapt>")
    parser.add_argument("p1", nargs='?', type=int, default=36, help="Technology change months")
    parser.add_argument("p2", nargs='?', type=int, default=36, help="Worker adaptation months")
    args = parser.parse_args()

    if args.p1 != int(args.p1) or args.p2 != int(args.p2):
        print("Values must be whole integers.")
        exit()

    # Define 20% tranches t1-t5 and normalize "months to adapt" for each tranche as percentages of total months
    t1, t2, t3, t4, t5 = args.p2 * 0.2, args.p2 * 0.4, args.p2 * 0.6, args.p2 * 0.8, args.p2 * 1.0
    y5, y4, y3, y2, y1 = t1 / args.p1 * 100, t2 / args.p1 * 100, t3 / args.p1 * 100, t4 / args.p1 * 100, t5 / args.p1 * 100

    # Print input values to stdout (may be commandline parameters of default)
    print("Technology change months (time available for workers to adapt):", args.p1,)
    print("Worker adapatation months (time needed for workers to adapt):", args.p2,)

    x, y, z = generate_data()
    save_csv(x, y, z)
    create_chart(x, y, z, t1, t2, t3, t4, t5, args.p1)
