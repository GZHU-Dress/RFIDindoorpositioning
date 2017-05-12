# RFIDindoorpositioning
A way to achieve localization algorithm by machine learning.


# 基於機器學習的RFID 室內定位算法

## 前言
> 本方法意在探索而非求成。RFID 室內定位的算法發展多年，個人感覺在精度方面的挖掘潛能不太大，主要受限與設備精度和成本。僅希望嘗試一個新的發展方向。

傳統方法是通過至少三根天線通過已知天線位置來推算出未知標籤的位置，此類方法需要先通過RSSI 值和人爲設定環境因子來換算出到參考天線的距離，然後通過極大似然法來計算天線所在的座標。

![圖示極大似然](https://github.com/axionl/RFIDindoorpositioning/blob/master/fig/%E6%A5%B5%E5%A4%A7%E4%BC%BC%E7%84%B6%E6%B3%95.svg)

還有一種基於傳統方法的改進，就是指紋標籤法。同樣至少使用三根天線，預先布放參考標籤，測得參考標籤的位置和對應的RSSI 值。然後在實際使用中撤走參考標籤，通過將測試標籤的RSSI 值與之前參考標籤的值進行比對得出測試標籤的位置或者是到天線的距離。
![圖示指紋標籤法](https://github.com/axionl/RFIDindoorpositioning/blob/master/fig/%E6%8C%87%E7%B4%8B%E6%A8%99%E7%B1%A4%E6%B3%95.svg)

## 思路
主要分爲兩種，一種是有三個天線及以上的，另外一種是一到兩個天線外加旋轉平臺的。

### 三天線及以上
按照天線個數分爲幾個大塊，然後在大塊中再建立多項式模型，這裏爲了簡述原理，僅取大塊爲一次式，即用直線擬合，如何內部細分不在此說明內。
利用为rssi 测量值添加权值的方法来得到定位结果，再利用实测结果调整权值，這裏爲了簡述原理，只是將大塊組合成了矩陣用於機器學習，內部沒有細分。

<img src="https://latex.codecogs.com/gif.latex?\left\{\begin{matrix}&space;\theta_{1}rssi_{1}^{1}&plus;\theta_{2}rssi_{1}^{2}&plus;...&plus;\theta_{n}rssi_{1}^{n}&space;=&space;X_1\\&space;\theta_{1}rssi_{2}^{1}&plus;\theta_{2}rssi_{2}^{2}&plus;...&plus;\theta_{n}rssi_{2}^{n}&space;=&space;X_2&space;\\&space;\vdots&space;\\&space;\theta_{1}rssi_{n}^{1}&plus;\theta_{2}rssi_{n}^{2}&plus;...&plus;\theta_{n}rssi_{n}^{n}&space;=&space;X_n&space;\\&space;\end{matrix}\right." title="\left\{\begin{matrix} \theta_{1}rssi_{1}^{1}+\theta_{2}rssi_{1}^{2}+...+\theta_{n}rssi_{1}^{n} = X_1\\ \theta_{1}rssi_{2}^{1}+\theta_{2}rssi_{2}^{2}+...+\theta_{n}rssi_{2}^{n} = X_2 \\ \vdots \\ \theta_{1}rssi_{n}^{1}+\theta_{2}rssi_{n}^{2}+...+\theta_{n}rssi_{n}^{n} = X_n \\ \end{matrix}\right." />

** <img src="https://latex.codecogs.com/gif.latex?\theta" title="\theta" /> 的下標表示這是第n 根天線測得的數據，也是我們要訓練的參數。rssi 值上標表示屬於第幾根天線，下標表示這是該天線測得的第幾個數據。X 下標就是這四個天線在同一時間測得訓練集的X 座標。**

然後將上面多項式然後轉化爲矩陣進行訓練。

<img src="https://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;rssi_1^{1}&space;&&space;rssi_1^{2}&space;&&space;rssi_1^{3}&space;&&space;\cdots&space;&&space;rssi_1^{n}&space;\\&space;rssi_2^{1}&space;&&space;rssi_2^{2}&space;&&space;rssi_2^{3}&space;&&space;\cdots&space;&&space;rssi_2^{n}&space;\\&space;\vdots&space;&&space;\vdots&space;&&space;\vdots&space;&&space;\cdots&space;&&space;\vdots&space;\\&space;rssi_n^{1}&space;&&space;rssi_n^{2}&space;&&space;rssi_n^{3}&space;&&space;\cdots&space;&&space;rssi_n^{n}&space;\\&space;\end{bmatrix}&space;\begin{bmatrix}&space;\theta_1&space;\\&space;\theta_2&space;\\&space;\vdots\\&space;\theta_n\\&space;\end{bmatrix}&space;=\begin{bmatrix}&space;X_1&space;\\&space;X_2&space;\\&space;\vdots\\&space;X_n\\&space;\end{bmatrix}" title="\begin{bmatrix} rssi_1^{1} & rssi_1^{2} & rssi_1^{3} & \cdots & rssi_1^{n} \\ rssi_2^{1} & rssi_2^{2} & rssi_2^{3} & \cdots & rssi_2^{n} \\ \vdots & \vdots & \vdots & \cdots & \vdots \\ rssi_n^{1} & rssi_n^{2} & rssi_n^{3} & \cdots & rssi_n^{n} \\ \end{bmatrix} \begin{bmatrix} \theta_1 \\ \theta_2 \\ \vdots\\ \theta_n\\ \end{bmatrix} =\begin{bmatrix} X_1 \\ X_2 \\ \vdots\\ X_n\\ \end{bmatrix}" />

如何訓練得到<img src="https://latex.codecogs.com/gif.latex?\theta" title="\theta" />有很多種方法，最爲簡單的就是梯度下降類，在此不作贅述。

實際上爲了達到更好的擬合效果需要視環境而定大塊中如何添加高次項以達到更好的擬合效果，同時要避免出現過擬合的現象，那麼還需要考慮加正則項來抑制過擬合。
另外也可以不直接從RSSI 一步到位得到座標，可以利用中間量d，再加以調參。

### 一天線及兩天線
此處考慮射頻天線指向性不夠精確故不推薦一天線的方案

![圖示雙天線法](https://github.com/axionl/RFIDindoorpositioning/blob/master/fig/%E6%85%A3%E6%80%A7%E5%88%A4%E5%AE%9A%E6%B3%95.svg）

爲其中一個天線添加一個轉軸，由步進電機控制左右擺動，根據轉動時同一個標籤ID 接收強度的不同，可以粗略判斷左交點還是右交點，再利用慣性算法來定位。同樣通過機器學習可以得到標籤的座標。
