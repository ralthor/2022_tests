CXX	:= g++
CXX_FLAGS := -Wall -Wextra -std=c++11 -g
LDFLAGS := -lglfw3 -lopengl32 -lgdi32

BIN	:= bin
SRC	:= src
INCLUDE	:= include

LIBRARIES	:=
EXECUTABLE	:= opengltest2.exe
CPPOBJECTS := $(patsubst $(SRC)/%.cpp,$(BIN)/%.o,$(wildcard $(SRC)/*.cpp))
COBJECTS := $(patsubst $(SRC)/%.c,$(BIN)/%.o,$(wildcard $(SRC)/*.c))

all: $(BIN)/$(EXECUTABLE)

run: clean all
	./$(BIN)/$(EXECUTABLE)

$(BIN)/$(EXECUTABLE): $(CPPOBJECTS) $(COBJECTS)
	echo $^
	$(CXX)  $^ -o $@ $(CXX_FLAGS) -I$(INCLUDE) $(LDFLAGS)

$(CPPOBJECTS): $(wildcard $(SRC)/*.cpp)
# for each cpp file, compile it into an object file and put it in bin
	$(CXX) $(CXX_FLAGS) -I$(INCLUDE) -c $(patsubst $(BIN)/%.o,$(SRC)/%.cpp,$@) -o $@

$(COBJECTS): $(wildcard $(SRC)/*.cpp)
# for each c file, compile it into an object file and put it in bin
	$(CXX) $(CXX_FLAGS) -I$(INCLUDE) -c $(patsubst $(BIN)/%.o,$(SRC)/%.c,$@) -o $@

test:
	echo $(CPPOBJECTS)
	echo $(COBJECTS)
	echo $(EXECUTABLE)

clean:
	-rm -f $(BIN)/*
