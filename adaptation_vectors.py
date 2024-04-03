import argparse
import numpy as np
import matplotlib.pyplot as plt

def generate_data():
    # Generate 2500 points in a 3D field conforming to a gaussian distribution
    np.random.seed(0)
    X = np.random.normal(loc=50, scale=20, size=2500)
    Y = np.random.normal(loc=50, scale=20, size=2500)
    Z = np.random.normal(loc=50, scale=20, size=2500)
    return X, Y, Z

def save_csv(X, Y, Z):
    # Save points in a local CSV file
    data = np.column_stack((X, Y, Z))
    np.savetxt("adaptation_vectors.csv", data, delimiter=",", header="X,Y,Z", comments='', fmt='%0.2f')

def create_chart(X, Y, Z, T1, T2, T3, T4, T5, P1):
    # Chart points delineated by Y axis value ("percent of workforce") color coding each 20% tier
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(111, projection='3d')

    # Define colors based on Y values
    colors = np.where(Y > Y2, 'green',  # Green
                      np.where(Y > Y3, 'blue',  # Lightblue
                               np.where(Y > Y4, 'violet',  # Orange
                                        np.where(Y > Y5, 'purple',  # Orangered
                                                 'red'))))  # Red

    ax.scatter(X, Y, Z, c=colors)

    # Set Y value demarcation at Y2 (between top 20% and bottom 80% of Y values) as a whole integer
    L4 = int(round(Y2))

    # Draw demarcation line on chart
    ax.plot([100, 0], [L4, L4], [0, 100], color='black')

    # Set chart axis increments and labels
    ax.set_xticks(np.arange(0, 101, 10))
    ax.set_xticklabels(["{}%".format(i) for i in range(0, 101, 10)], fontsize=6)
    ax.set_xlabel("X = Time Available", fontsize=9)

    ax.set_yticks(np.arange(0, 101, 10))
    ax.set_yticklabels(["{}%".format(i) for i in range(0, 101, 10)], fontsize=6)
    ax.set_ylabel("Y = Percent of Workforce", fontsize=9)

    ax.set_zticks(np.arange(0, 101, 10))
    ax.set_zticklabels(["{}%".format(i) for i in range(0, 101, 10)], fontsize=6)
    ax.set_zlabel("Z = Ability to Adapt", fontsize=9)

    plt.savefig("adaptation_vectors.png")
    plt.close()

if __name__ == "__main__":
    # Parse commandline and emit messages on error, set default values if no input is provided
    parser = argparse.ArgumentParser(description="adaptation_vectors.py <total months> <max months to adapt>")
    parser.add_argument("P1", nargs='?', type=int, default=60, help="Total months")
    parser.add_argument("P2", nargs='?', type=int, default=60, help="Max months to adapt")
    args = parser.parse_args()

    if args.P1 != int(args.P1) or args.P2 != int(args.P2):
        print("Values must be whole integers.")
        exit()

    # Define 20% tranches T1-T5 and normalize "months to adapt" for each tranche as percentages of total months
    T1, T2, T3, T4, T5 = args.P2 * 0.2, args.P2 * 0.4, args.P2 * 0.6, args.P2 * 0.8, args.P2 * 1.0
    Y5, Y4, Y3, Y2, Y1 = T1 / args.P1 * 100, T2 / args.P1 * 100, T3 / args.P1 * 100, T4 / args.P1 * 100, T5 / args.P1 * 100

    # Print input values to stdout (may be commandline parameters of default)
    print("Time available (in months) for workers to adapt (default 60 months):", args.P1,)
    print("Time required (in months) for workers to adapt (default 60 months):", args.P2,)

    X, Y, Z = generate_data()
    save_csv(X, Y, Z)
    create_chart(X, Y, Z, T1, T2, T3, T4, T5, args.P1)
