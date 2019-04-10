class CustomException(Exception):
    print("failed")
    pass


if __name__=="__main__":
    try:
        out="tried"
        #assert 1==2
        raise CustomException(out)
    except CustomException as print_out:
        print(print_out)