import time

def ve_hinh():
    # hinh1 = [
    #     "      *   ",
    #     "      * *  ",
    #     "      * * * ",
    #     "* * * * * * *",
    #     "* * * ",
    #     "* * ",
    #     "*   "
    # ]

    # hinh2 = [
    #     "      *   ",
    #     "      * *  ",
    #     "      *   * ",
    #     "* * * * * * *",
    #     "*   * ",
    #     "* * ",
    #     "*   "
    # ]

    # hinh3 = [
    #     "      * * * *  ",
    #     "      * * *",
    #     "      * *",
    #     "      * ",
    #     "    * * ",
    #     "  * * *  " ,
    #     "* * * * "  ,
    # ]

    # hinh4 = [
    #     "         * * * *  ",
    #     "         *   *",
    #     "         * *",
    #     "         * ",
    #     "       * * ",
    #     "     *   * " ,
    #     "   * * * * "  ,
    # ]
    test_list= [[
        "      *   ",
        "      * *  ",
        "      * * * ",
        "* * * * * * *",
        "* * * ",
        "* * ",
        "*   "],[
        "      *   ",
        "      * *  ",
        "      *   * ",
        "* * * * * * *",
        "*   * ",
        "* * ",
        "*   "],[
        "      * * * *  ",
        "      * * *",
        "      * *",
        "      * ",
        "    * * ",
        "  * * *  " ,
        "* * * * "  ,],[
        "         * * * *  ",
        "         *   *",
        "         * *",
        "         * ",
        "       * * ",
        "     *   * " ,
        "   * * * * "  ,
    ]
]
    _list = [[0,1,2],[3,4,5],[6,7,8]]
    # hinh_list = [hinh1, hinh2, hinh3, hinh4]
    # while True:
    for hinh in test_list:
        print(hinh)
        # for line in hinh:
            # print(line)
        # print("*")
        # time.sleep(5)  # Chờ 5 giây trước khi xuất hiện hình tiếp theo

# ve_hinh()
for i in range(0,10):
    for j in range(0,10):
        for k in range(0,5):
            print(i,j,k, "=", i+(j*k))
