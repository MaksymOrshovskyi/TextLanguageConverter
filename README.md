# Example

# English into Ukrainian 
ghbdsn -> привіт

# Ukrainian into English
руддщ -> hello

# How to create Docker image and run container
- Open your terminal or command prompt, navigate to the directory containing your Dockerfile and Python script

Then use this commands
1) docker build -t text-language-converter .  
   (to create an image with name "text-language-converter")
2) docker run -i --name container-text-converter text-language-converter
   (to create a container with name "container-text-converter")
3) if you want to start the container again, use the next commands:
   1)docker start container-text-converter
   
   2)docker attach container-text-converter