#include <iostream>

using namespace std;

class Strategy {
public:
  virtual void doAction() = 0;
};

class Option1Strategy : public Strategy {
public:
  void doAction() override {
    cout << "Opcion 1 seleccionada" << endl;
  }
};

class Option2Strategy : public Strategy {
public:
  void doAction() override {
    cout << "Opcion 2 seleccionada" << endl;
  }
};

class Context {
public:
  Context(Strategy* strategy) {
    this->strategy = strategy;
  }

  void doAction() {
    strategy->doAction();
  }

private:
  Strategy* strategy;
};


int main() {
  int option;

  cout << "Elija una opcion:" << endl;
  cout << "1. Opcion 1" << endl;
  cout << "2. Opcion 2" << endl;
  cin >> option;

  // Creo una instancia de la estrategia correspondiente y se asigna al contexto.
  Strategy* strategy;
  switch (option) {
    case 1:
      strategy = new Option1Strategy();
      break;
    case 2:
      strategy = new Option2Strategy();
      break;
    default:
      cout << "Opcion no válida." << endl;
      return 1;
  }

  Context context(strategy);

  context.doAction();

  return 0;
}