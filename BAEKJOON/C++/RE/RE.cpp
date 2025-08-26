#include <iostream>

class Marine{
  private:
    int hp;
    int coord_x, coord_y;
    int damage;
    bool is_dead;
    
  public:
    Marine();
    Marine(int x, int y);

    int attack();
    void be_attacked(int damage_earn);
    void move(int x, int y);
    void show_status();
};

Marine::Marine(){
  hp = 50;
  coord_x = coord_y = 0;
  damage = 5;
  is_dead = false;
}

Marine::Marine(int x, int y){
  coord_x = x;
  coord_y = y;
  hp = 50;
  damage = 5;
  is_dead = false;
}

void Marine::move(int x, int y){
  coord_x = x;
  coord_y = y;
}

int Marine::attack(){
  return damage;
}

void Marine::be_attacked(int damage_earn){
  hp -= damage_earn;
  if (hp <=0){
    is_dead = true;
  }
}

void Marine::show_status() {
  std::cout << " *** Marine *** " << std::endl;
  std::cout << " Location : ( " << coord_x << " , " << coord_y << " ) "
            << std::endl;
  std::cout << " HP : " << hp << std::endl;
}

int main(){
  Marine mar1(2, 3);
  Marine mar2(10, 6);

  mar1.show_status();
  mar2.show_status();

  std::cout << "mar1 att mar2" << std::endl;

  mar2.be_attacked(mar1.attack());

  mar1.show_status();
  mar2.show_status();

  std::cout << "mar1 move to (7, 48)" << std::endl;
  std::cout << "mar2 move to (69, 10)" << std::endl;
  mar1.move(7,48);
  mar2.move(69,10);

  mar1.show_status();
  mar2.show_status();

}