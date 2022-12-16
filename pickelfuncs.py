import pickle


def save_object(data):
    try:
        with open("busrouts.pickle", "wb") as f:
            #delete file before
            pickle.dump(data, f)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)


def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)
