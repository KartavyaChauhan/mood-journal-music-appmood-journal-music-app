def get_affirmation(mood):
    """Generate affirmations based on mood"""
    return get_fallback_affirmation(mood)

def get_fallback_affirmation(mood):
    """Curated affirmations for different moods"""
    affirmations = {
        "happy": "Your joy is contagious and brings light to those around you. Keep shining bright! ✨",
        "sad": "It's okay to feel sad sometimes. You are strong and this feeling will pass. 💙",
        "anxious": "Take a deep breath. You have overcome challenges before and you will overcome this too. 🌸",
        "stressed": "You are doing your best, and that is enough. Take time to rest and recharge. 🌿",
        "angry": "Your feelings are valid. Channel this energy into positive change. 🔥",
        "excited": "Your enthusiasm is wonderful! Embrace this positive energy and let it guide you. ⚡",
        "calm": "Your inner peace is a gift. Continue to nurture this beautiful state of mind. 🕊️",
        "confused": "It's okay not to have all the answers right now. Clarity will come with time. 🌅",
        "grateful": "Gratitude opens your heart to abundance. You attract what you appreciate. 🙏",
        "lonely": "You are never truly alone. You are loved and valued more than you know. 💝",
        "tired": "Rest is not a luxury, it's a necessity. Honor your body's need for restoration. 😴",
        "motivated": "Your drive and determination will take you far. Keep moving forward! 🚀",
        "peaceful": "This moment of peace is precious. Let it fill your soul with tranquility. ☮️",
        "optimistic": "Your positive outlook is a superpower. Keep believing in bright possibilities. 🌈"
    }
    
    mood_lower = mood.lower()
    for key in affirmations:
        if key in mood_lower:
            return affirmations[key]
    
    return "You are worthy of love, peace, and happiness. Trust in your journey and believe in yourself. ✨"
