import os

def get(file_ql=None, layer=None):
    # 変数
        # 入力
    file_ql = str(file_ql)
    layer = str(layer)
        # 格納
    file_list = None # ファイル分割データ
    not_inject_list = ["\"", ":", "?", "<", ">", "|"] # 入力不可な文字列
        # 出力
    output = None
        # その他
    while_x = 0 #while カウント
    while_y = 0 #while カウント
    check_x = []

    # 入力がない時の処理をここに入れる
    print("dev" + file_ql)
    if file_ql == "None":
        output = None
        print("Error: Incorrect file value.\nInfo: (__file__,\"Layer\")の形式で入力する必要があります。")
        return(output)
    if layer == "None":
        output = None
        print("Error: Incorrect layer value.\nInfo: (__file__,\"Layer\")の形式で入力する必要があります。")
        return(output)

    # file_qlの処理
    file_list = file_ql.split(os.sep)
    del file_list[-1]

            # エラー処理系
    # 利用不可文字の判定
    while True:
        if not_inject_list[while_x] in layer:
            output = None
            print("Error: Incorrect layer value.\nInfo: 入力値に利用できない文字が含まれています。")
            return(output)
        
        # brake判定
        if while_x == len(not_inject_list) - 1:
            break
        else:
            while_x = while_x + 1

    # Layerの処理
    layer = layer.split('/')

    # 空白が含まれていないか
    if "" in layer:
        output = None
        print("Error: Incorrect layer value.\nInfo: 入力値に空白が含まれています。")
        return(output)

    # ドット単体が含まれていないか
    if "." in layer:
        output = None
        print("Error: Incorrect layer value.\nInfo: 入力値にドット(単体)が含まれています。")
        return(output)

    # ..が中間に含まれていた場合のエラー処理
    while True:
        # ..を使っているか/含まれているか
        if layer[0] in "..":
            pass
        else:
            if ".." in layer:
                output = None
                print("Error: Incorrect layer value.\nInfo: ..(上位層移動文字)が不適切な位置に存在します。")
                return(output)
            else:
                break

        # ..が中間に含まれているか
        if layer[while_y] in "..":
            check_x.append("Y")
            if check_x[while_y - 1] in "N":
                output = None
                print("Error: Incorrect layer value.\nInfo: ..(上位層移動文字)が不適切な位置に存在します。")
                return(output)
        else:
            check_x.append("N")

        # brake判定
        if while_y == len(layer) - 1:
            break
        else:
            while_y = while_y + 1
            #ここまで

    # ..分リストを後ろから消す 先端が(..)なら消して階層の末尾を消す。ここも階層消せなくなったらエラー消しすぎです！
    while True:
        if layer[0] == "..":
            if len(file_list) > 1:
                del layer[0]
                del file_list[-1]
            else:
                output = None
                print("Error: Incorrect layer value.\nInfo: 入力値が移動できる上位層を超えています。")
                return(output)

            if len(layer) == 0:
                break
        else:
            break

    # 出力成形
    output= os.sep.join(file_list) + os.sep + os.sep.join(layer)
    return(output)

    print("FileList: " + str(file_list))
    print("LayerList: " + str(layer))

    # 
    
    #len(file_list)