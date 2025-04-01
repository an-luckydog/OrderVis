# OrderVis
This is an interface of OrderVis. It is a tool that can improve the explainability of DTM(Deep Temporal Model).


## How to use
This system includes two parts: browser side and machine learning side. The machine learning side calculates interpretable information of DTM set by researchers based on users' input, as well as predicted value of input after reordering by end-users. The machine learning side can be run directly and offers partial interpretability.   
The code is available under machine learning branch: https://github.com/505025234/OrderVis/tree/machine-learning-side .


While the browser side is responsible for visualization and interaction. It will work with the machine learning side and improve interpretability greatly.   
The code is available under browser side branch https://github.com/505025234/OrderVis/tree/browser-side



  `If you need to use our system, please run the browser side and machine learning side on the same or two machines.` 

  `If you just want to check efficiency of the system, please visit http://52.82.121.31:81/ and use examples we have provided.`


## Critical Interface
  - 1.The researchers need to import target model in interface StartPro, and run the machine learning side through this interface.  
  - 2.While the program is running, the machine learning side will call interface oriInputSigni to calculate interpretable information of DTM.  
  - 3.Interface getPredict is set to provide end-users with predicted values of reordered inputs.  
  - 4.If you want to use our system to trace training data, it is essential to pre-processing your data. You should use interface ReadFile to import your model and read your data into cash. Details of usage will be shown in maching learning branch.  
![image](https://github.com/505025234/OrderVis/blob/main/interFace.png)

## Main function
### Machine learning side (back-end)
  - 1.ReadFile and PreTreat are used to pre-process training data. (Pre-processing is not necessary. However, if you want to trace your training data, it must be done before establishing a server on the machine learning side.)  
  - 2.ServertoStart and StartPro are used to import model which will be interpreted.  
  - 3.ReorderByGroup is used to calculate local interpretability and glabal interpretability of model; GetDiffer is used to capture critical order line using Genetic Algorithm; GetPartner is used to trace training data(not available without pre-processing).  
  - 4.GetPredict is used to compute predictions for inputs that have been reordered by end-users.  
### Browser side (front-side)
  - 1.GetInput will communicate with the machine learning side and call ReorderByGroup, GetDiffer, GetPartner. It will graphically display the interpretable information of the DTM.  
  - 2.DragData will be called and communicate with the machine learning side when end-users interact with the system by dragging components or tokens. DragData will display predicted values of reordered inputs.
![image](https://github.com/505025234/OrderVis/blob/main/generalizationProcedure.png)

## Example View

![image](https://github.com/505025234/OrderVis/blob/main/localhost_8080_.png)

## Trace Example

![image](https://github.com/505025234/OrderVis/blob/main/TraceExample.png)
