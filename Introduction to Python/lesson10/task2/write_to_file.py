zoo = ['lion', "elephant", 'monkey']

if __name__ == "__main__":
    f = open("output.txt", "a")
    z = 1
    for i in zoo:
        f.write(i)
        z += 1
        if (len(zoo) + 1) != z: f.write(", ")

    f.close()
