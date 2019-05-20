# coding:utf-8


if __name__ == '__main__':
    k =1
    while k < 1001:
        features_path = "E:/test1000/1比1id1000features"
        # 1:N证件照的features路径
        features_path_N = "E:/test1000/1比Nid1000features"
        with open((features_path+"/"+"%d" % k+".jpg.txt"),"r") as fp:
            features_1 = fp.read()
            # print(features_1)
            a = "澶辫触"
        if features_1 == a:
            print(k)
        k+=1
    # features_path = "E:/test1000/1比1id1000features"
    # with open((features_path + "/" + "67" + ".jpg.txt"), "r") as fp:
    #     features_1 = fp.read()
    #     print(features_1)
