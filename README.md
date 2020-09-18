# Contour_Draw_3D  


3D ジオメトリを輪切りして切り出した断面の連番画像から、擬似的に 3D ジオメトリを描画するライブラリ。  

このライブラリでは、擬似的なレンダリングを行なっているが、連番画像から、立体を描画する技術は、CT スキャンなどの医療分野に向けて古くから研究され、1987年には、現在でも多く使われる Marching Cube アルゴリズムが発表されている。  

今回は、3D データを計算する必要がないので、高速で処理できればという感じで、画像処理による擬似レンダリングで描画する方法を採用した。  

このライブラリは、同時並行で作っているボクセル 3D Printing ライブラリで生成した連番画像から出力の確認を行うために制作している。  


### Process  

1) 断面の画像をアフィン変換により平行四辺形に変形し、斜め上から見た画像に置き換える。  

2) 斜め上から見た連番画像を適切な位置に貼り重ねることで、立体の絵を擬似的にレンダリングする。  

ここでは、適切な位置というのは、マジックナンバーを探す（いまのところ）という様になっている。  
正確にいうと、斜め上から見た様に変形するためのマトリクスというも同様にマジックナンバーである。  
この辺は、普通に計算で出るはずなので、そのへんもいつか実装予定。  


### Related Projects  

- Mesh_Vertex_Color    
  // ドット・バイ・ドットのボクセル入稿ができるフルカラー 3D Printing に向けて、メッシュを数理的に解くライブラリ  
  [https://github.com/naysok/Mesh_Vertex_Color](https://github.com/naysok/Mesh_Vertex_Color)  



### Ref  

- Marching cube（Wikipedia）  
  [https://en.wikipedia.org/wiki/Marching_cubes](https://en.wikipedia.org/wiki/Marching_cubes)  

- デジタル画像と定量化 その6：アフィン変換・位置合わせ（九州大学 大学院 非常勤講師 吉澤 信）  
[http://www2.riken.jp/brict/Yoshizawa/Lectures/Kyuusyu/Lectures2011_06.pdf](http://www2.riken.jp/brict/Yoshizawa/Lectures/Kyuusyu/Lectures2011_06.pdf)  

 