class CryptoBuddy:
    def __init__(self):
        self.name = "CryptoBuddy"
        self.tone = "meme-loving"

    def introduce(self):
        return (
            f"Hey there! I'm {self.name} 🚀, your meme-loving crypto sidekick! "
            "Ask me anything about crypto, and I'll try to explain it with a sprinkle of memes and good vibes. "
            "Let's make crypto fun and easy, one meme at a time! 😎💰"
        )

    def respond(self, message):
        # Example meme-style response
        if "bitcoin" in message.lower():
            return "Bitcoin? To the moon! 🚀🌕 HODL on tight, fren!"
        elif "ethereum" in message.lower():
            return "Ethereum is like the cool kid at the blockchain party. Smart contracts FTW! 🤓"
        elif "cardano" in message.lower():
            return "Cardano? It's like the blockchain that took a nap and woke up ready to build! 😴➡️🏗 ️"
        else:
            return "Crypto questions? Hit me up! I promise to keep it 100 and meme-tastic. 🙌"

# Example usage:
if __name__ == "__main__":
    bot = CryptoBuddy()
    import sys
    print(bot.introduce().encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))
    user_input = input("You: ")
    print(f"{bot.name}: {bot.respond(user_input)}".encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))

# Predefined Crypto Data
crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3/10  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10  
    }  
}  

def answer_query(user_query):
    query = user_query.lower()
    if "sustainable" in query or "eco" in query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"Invest in {recommend}! 🌱 It’s eco-friendly and has long-term potential!"
    elif "trending up" in query or "rising" in query or "upward" in query:
        trending = [name for name, data in crypto_db.items() if data["price_trend"] == "rising"]
        if trending:
            return f"These cryptos are trending up: {', '.join(trending)} 🚀"
        else:
            return "No cryptos are trending up right now. 😅"
    elif "market cap" in query or "biggest" in query:
        biggest = max(crypto_db, key=lambda x: crypto_db[x]["market_cap"])
        return f"{biggest} has the highest market cap! 💸"
    else:
        return "Try asking: 'Which crypto is trending up?' or 'What’s the most sustainable coin?'"

# Example usage:
if __name__ == "__main__":
    bot = CryptoBuddy()
    print(bot.introduce().encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))
    user_input = input("You: ")
    print(f"{bot.name}: {bot.respond(user_input)}".encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))
    print("CryptoBuddy (data-driven):", answer_query(user_input))
    def give_advice(user_query):
        query = user_query.lower()
        # Profitability advice
        if "profit" in query or "profitable" in query:
            profitable = [
                name for name, data in crypto_db.items()
                if data["price_trend"] == "rising" and data["market_cap"] == "high"
            ]
            if profitable:
                return f"For max profit, check out: {', '.join(profitable)} 🚀💰"
            else:
                return "No highly profitable coins at the moment. Keep an eye out! 👀"
            # Also check for "profitable" and "profit" in more flexible ways
            if any(word in query for word in ["profit", "profitable", "make money", "gain"]):
                profitable = [
                    name for name, data in crypto_db.items()
                    if data["price_trend"] == "rising" and data["market_cap"] == "high"
                ]
                if profitable:
                    return f"For max profit, check out: {', '.join(profitable)} 🚀💰"
                else:
                    return "No highly profitable coins at the moment. Keep an eye out! 👀"
    #example usage:
    def give_advice(user_query):
        query = user_query.lower()
        # Profitability advice
        if "profit" in query or "profitable" in query:
            profitable = [
                name for name, data in crypto_db.items()
                if data["price_trend"] == "rising" and data["market_cap"] == "high"
            ]
            if profitable:
                return f"For max profit, check out: {', '.join(profitable)} 🚀💰"
            else:
                return "No highly profitable coins at the moment. Keep an eye out! 👀"

        # Sustainability advice
        if "sustain" in query or "eco" in query or "green" in query:
            sustainable = [
                name for name, data in crypto_db.items()
                if data["energy_use"] == "low" and data["sustainability_score"] > 7/10
            ]
            if sustainable:
                return f"Eco-friendly picks: {', '.join(sustainable)} 🌱"
            else:
                return "No coins meet the top sustainability criteria right now. 🌍"
        return None

    # Example usage:
    if __name__ == "__main__":
        bot = CryptoBuddy()
        print(bot.introduce().encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))
        user_input = input("You: ")
        advice = give_advice(user_input)
        if advice:
            print(f"{bot.name} (advice): {advice}".encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))
        print(f"{bot.name}: {bot.respond(user_input)}".encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))
        print("CryptoBuddy (data-driven):", answer_query(user_input))
    class AICryptoBuddy(CryptoBuddy):
        def __init__(self):
            super().__init__()

        def respond(self, message):
            # Try data-driven answer first
            data_answer = answer_query(message)
            # If data-driven answer is generic, fallback to meme-style
            if "Try asking:" in data_answer:
                return super().respond(message)
            else:
                return data_answer

    if __name__ == "__main__":
        bot = AICryptoBuddy()
        print(bot.introduce().encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print(f"{bot.name}: Catch you later! 🚀")
                break
            print(f"{bot.name}: {bot.respond(user_input)}".encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))