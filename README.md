# A containerized application for serving your Scikit Models as an API
Screenshot:



![](https://github.com/skandupmanyu/Model_Serving_App/blob/master/screenshot/interface.png)

Build container image:
```
docker build -t serving_app .
```

Run application:
```
docker run -p 5000:5000 --name=serving_model serving_app
```

- Go to "Your local IP address":5000 in your browser (example: http://192.168.1.132:5000/)
- Upload your model (you can use the one in the sample_model folder and observe the code used for training)
- Open terminal and make an API request using:

```
curl --header "Content-Type: application/json" \
--request POST \
--data '{"housing_median_age":15.0,"total_rooms":5612.0,"total_bedrooms":1283.0,"population":1015.0,"households":472.0,"median_income":1.4936}' \
http://"Your local IP address":5000/predict
```

Replace the values of --data with the data you want to make a prediction for.
