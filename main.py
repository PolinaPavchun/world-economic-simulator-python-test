import matplotlib.pyplot as plt
import numpy as np

class CountryAttackSimulator:
    """Симулятор"""
    def __init__(self):
        self.base_costs = {
            'Энергоколлапс': 80,
            'Финансовая паника': 120,
            'Кибератака': 140,
            'Торговая война': 90,
            'Валютный кризис': 110,
            'Дефолт': 160,
            'Сырьевая блокада': 130,
            'Социальный протест': 80
        }
        self.countries = {
            'Страна А': 1.0,
            'Страна Б': 1.2,
            'Страна В': 0.8,
            'Страна Г': 1.5
        }
        
        self.country_health = {country: 100 for country in self.countries}
        
    def calculate_attack_cost(self, attack_name, country_name):
        """Рассчитать стоимость атаки для конкретной страны"""
        base_cost = self.base_costs[attack_name]
        weight = self.countries[country_name]
        return base_cost * weight
    
    def apply_attack(self, attack_name, country_name):
        """Применить атаку к стране"""
        if attack_name not in self.base_costs:
            print(f"Атака '{attack_name}' не найдена!")
            return False
        
        if country_name not in self.countries:
            print(f"Страна '{country_name}' не найдена!")
            return False
        
        
        damage = self.calculate_attack_cost(attack_name, country_name)
        
        
        self.country_health[country_name] -= damage
        
        
        if self.country_health[country_name] < 0:
            self.country_health[country_name] = 0
            
        print(f"Атака '{attack_name}' нанесла {damage:.1f} урона стране '{country_name}'")
        print(f"Здоровье {country_name}: {max(0, self.country_health[country_name]):.1f}")
        
        return True
    
    def check_winner(self):
        """Проверить, есть ли победитель"""
        alive_countries = [country for country, health in self.country_health.items() if health > 0]
        
        if len(alive_countries) == 0:
            return "Все страны проиграли!"
        elif len(alive_countries) == 1:
            return f"Победитель: {alive_countries[0]}"
        else:
            return None
    
    def visualize_health(self):
        """Визуализировать здоровье стран"""
        countries = list(self.country_health.keys())
        health_values = list(self.country_health.values())
        
        colors = []
        for health in health_values:
            if health <= 0:
                colors.append('red')  
            elif health < 30:
                colors.append('orange')  
            else:
                colors.append('green')  
        
        plt.figure(figsize=(10, 6))
        bars = plt.bar(countries, health_values, color=colors, edgecolor='black')
        
        plt.title('Состояние стран после атак', fontsize=16, fontweight='bold')
        plt.xlabel('Страны', fontsize=12)
        plt.ylabel('Здоровье', fontsize=12)
        plt.ylim(0, 110)
        
        
        for bar, health in zip(bars, health_values):
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{health:.1f}',
                    ha='center', va='bottom' if health > 0 else 'top',
                    fontweight='bold')
        
        
        plt.axhline(y=0, color='r', linestyle='--', alpha=0.5, label='Поражение')
        
        plt.legend()
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        plt.show()
    
    def visualize_attack_power(self, attack_name):
        """Визуализировать силу атаки для разных стран"""
        if attack_name not in self.base_costs:
            print(f"Атака '{attack_name}' не найдена!")
            return
        
        countries = list(self.countries.keys())
        attack_powers = [self.calculate_attack_cost(attack_name, country) for country in countries]
        
        plt.figure(figsize=(10, 6))
        bars = plt.bar(countries, attack_powers, color='steelblue', edgecolor='black')
        
        plt.title(f'Сила атаки: {attack_name}', fontsize=16, fontweight='bold')
        plt.xlabel('Страны', fontsize=12)
        plt.ylabel('Урон', fontsize=12)
        
        
        for bar, power in zip(bars, attack_powers):
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{power:.1f}',
                    ha='center', va='bottom',
                    fontweight='bold')
        
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        plt.show()
    
    def show_available_attacks(self):
        """Показать доступные атаки"""
        print("\n" + "="*50)
        print("ДОСТУПНЫЕ АТАКИ:")
        print("="*50)
        for i, (attack, cost) in enumerate(self.base_costs.items(), 1):
            print(f"{i}. {attack}: {cost} (базовая стоимость)")
    
    def show_countries(self):
        """Показать страны и их уязвимость"""
        print("\n" + "="*50)
        print("СТРАНЫ И ИХ УЯЗВИМОСТЬ:")
        print("="*50)
        for i, (country, weight) in enumerate(self.countries.items(), 1):
            print(f"{i}. {country}: множитель уязвимости = {weight}")
    
    def run_interactive_simulation(self):
        """Запустить интерактивную симуляцию"""
        print("="*60)
        print("СИМУЛЯТОР АТАК НА СТРАНЫ")
        print("="*60)
        
        round_count = 1
        
        while True:
            print(f"\n{'='*30}")
            print(f"РАУНД {round_count}")
            print(f"{'='*30}")
            
            
            print("\nТекущее состояние стран:")
            for country, health in self.country_health.items():
                status = "ПОРАЖЕНА" if health <= 0 else f"{health:.1f}"
                print(f"  {country}: {status}")
            
            
            winner = self.check_winner()
            if winner:
                print(f"\n{'!'*50}")
                print(f"ИГРА ОКОНЧЕНА!")
                print(winner)
                print(f"{'!'*50}")
                self.visualize_health()
                break
            
            
            self.show_available_attacks()
            
            
            self.show_countries()
            
            
            try:
                attack_num = int(input("\nВыберите номер атаки (0 для выхода, -1 для визуализации): "))
                
                if attack_num == 0:
                    print("Выход из симуляции...")
                    break
                elif attack_num == -1:
                    self.visualize_health()
                    continue
                
                attack_name = list(self.base_costs.keys())[attack_num - 1]
                
                
                country_num = int(input("Выберите номер страны для атаки: "))
                country_name = list(self.countries.keys())[country_num - 1]
                
                
                self.apply_attack(attack_name, country_name)
                
                round_count += 1
                
            except (ValueError, IndexError):
                print("Некорректный ввод! Пожалуйста, выберите правильные номера.")
                continue


def example_simulation():
    """Пример предустановленной симуляции"""
    simulator = CountryAttackSimulator()
    
    print("Пример автоматической симуляции:")
    print("-" * 40)
    
    
    attacks = [
        ('Энергоколлапс', 'Страна А'),
        ('Финансовая паника', 'Страна Б'),
        ('Дефолт', 'Страна Г'),
        ('Кибератака', 'Страна В'),
        ('Торговая война', 'Страна А'),
        ('Сырьевая блокада', 'Страна Б'),
    ]
    
    for attack, country in attacks:
        print(f"\nАтака: {attack} -> {country}")
        simulator.apply_attack(attack, country)
    
    
    winner = simulator.check_winner()
    print(f"\nРезультат: {winner}")
    
    
    simulator.visualize_health()
    
    
    simulator.visualize_attack_power('Дефолт')


if __name__ == "__main__":
    
    simulator = CountryAttackSimulator()
    
    choice = input("Запустить интерактивную симуляцию? (y/n): ").lower()
    
    if choice == 'y':
        simulator.run_interactive_simulation()
    else:
        
        example_simulation()
