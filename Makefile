CXX := g++
CPPFLAGS := -Icpp/include
CXXFLAGS := -std=c++11 -Wall -Wextra -Werror -pedantic
LDFLAGS := -Lcpp/lib -lcpp -lglfw3 -lopengl32 -lgdi32

SRCPATH := cpp

files := opengltest2 glad

$(files):
	$(CXX) -g $(SRCPATH)/$@ -c $(CPPFLAGS) $(CXXFLAGS) $(LDFLAGS) $^ -o $@.o

# linking the object files
opengltest2: $(files)
	$(CXX) -g $(SRCPATH)/$@.cpp -c $(CPPFLAGS) $(CXXFLAGS) $(LDFLAGS) $^ -o $@.o

all: $(files)
