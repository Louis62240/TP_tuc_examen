from locust import HttpUser, task, between


class Simulation(HttpUser):
    wait_time = between(2,5)

    trainer_1_id: int
    trainer_2_id: int = 2

    pokemon_1_id: int
    pokemon_2_id: int = 2

    @task
    def get_home(self):
        response = self.client.post("/trainers/", json={"name": "Katana", "birthdate": "2022-11-07"})
        self.trainer_1_id = response.json()["id"]
        response = self.client.post("/trainers/"+str(self.trainer_1_id)+"/pokemon/", json={"api_id": 768, "custom_name": "Katagami"})
        self.pokemon_1_id = response.json()["id"]

        self.pokemon_2_id = self.client.get("/trainers/"+str(self.trainer_2_id)).json()["pokemons"][0]["api_id"]

        response = self.client.get("/pokemons/battle/"+str(self.pokemon_1_id)+"/"+str(self.pokemon_2_id)).json()
        
