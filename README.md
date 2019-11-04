名称：モーフゆらゆらツールv1.0.0
作者：Under(@qsuwandmore)

-----------------------------------------------------------------------------------
注意！！
本ツールはそぼろ様作　VMD Editorと合わせての使用を前提に作られています。VMD Editorで変換しない限りmmdでは使えないので予めご了承ください。
-----------------------------------------------------------------------------------
～機能～
任意の長さでモーフを揺らすモーションファイルを比較的手軽に作れます。目をうるうるさせたり耐えてる感じを出したいときに。

～使い方～
・motool.exeを開く
・パラメータを打ち込む
・runボタンを押す
・result.csvが出力されるのでVMD Editorでインポートし、vmdファイルとして保存する
・mmdで読み込んで使う

～パラメータ(上から順に)～
モーフ名：揺らすモーフの名称です。
基準値：モーフの値が揺れるとき中心になる値です。
基準値の目標値：終フレーム時の基準値です。基準値は基準値の目標値に向かって等速で変化します。
周期：揺れの周期です。波の周期ではなく基準値→最大→基準値→最小と周期ごとに動くようになります。
振幅：揺れの振幅です。
振幅の目標値：終フレーム時の振幅です。基準値同様目標値に向かって等速で変化します。
長さ：揺れの長さです。周期と合わない場合長さに達する直前の揺れで止まります。

備考
パラメータには初期値として笑いモーフを揺らすものが入っています。
出力されるcsvはresult.csvで固定、そのまま上書きされるようになっているので、VMDEditor側で命名してください。
出力してからmmd側でフレームをずらしたりすると変化を付けられます。土台をつくる手間を省くツールとして使っていただければ幸いです。

更新履歴
v1.0.0