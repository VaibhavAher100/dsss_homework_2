from setuptools import setup, find_packages

setup(
    name="math_quiz",  # Replace with your package name
    version="0.1.0",  # Replace with your version
    author="Vaibhav Aher",  # Replace with your name
    author_email="vaibhavaher100@example.com",  # Replace with your email
    description="A simple math quiz project",
    long_description=open("README.md").read(),  # Optional: Load from README.md
    long_description_content_type="text/markdown",  # Markdown formatting
    url="https://github.com/VaibhavAher100/dsss_homework_2.git",  # Project URL
    packages=find_packages(),  # Automatically find package directories
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Change license if needed
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version required
    install_requires= open("requirements.txt").read().splitlines() 
        # Add your dependencies here 
        
)