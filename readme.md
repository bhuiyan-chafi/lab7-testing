# Activities

The professor gave two files app_test.py and app.py in calc and string app. He asked to perform test in isolation and integration. And test is isolation is guided to perform with unit testing(pytest). There are confusions which is not clear by the demonstration, so what I will be doing is:

1. Putting _pytest_ in the requirements.txt file.
2. In the app_test.py I will rewrite one function mul() without rest functionalites just to test the arithmatical operation.
3. In the very same file I will write test cases for the multiplication function.
4. Use the Dockerfile_test file to build the image and container
   docker build -t calc_test -f Dockerfile_test .
5. Get inside the bash and test it
   docker run -p 5005:5000 --name calctest calc_test

# <span style="color:red">But is it what the professor asked?</span>

I don't know but maybe not. In the app_test.py file he did import the app.py file as main_app which means the app_test.py is meant to be
used for testing purposes not to extract the arithmatical operations. So, I have understood correctly! Start practicing the code from **Client Based Testing** point.

# Postman

Lab7-Testing holds the Unit Testing as mentioned in the lab. But note that we only tested one endpoint **add()** with postman. Check the script area and you will find out the testing js codes there.

# Locust test

Install locust: most probably install it will be installed globally since we are not using any virtual environment. But what to do!!

      pip install locust

Locust runs on the following host and port:

      http://localhost:8089

Hit the url and add your application url:

      http://localhost:5005
