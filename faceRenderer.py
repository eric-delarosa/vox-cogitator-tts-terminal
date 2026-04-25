class FaceRenderer:
    def __init__(self, face):
        self.face = face

    def render(self):
        # Placeholder for rendering logic
        print(f"Rendering face with vertices: {self.face.vertices}")    
    # map phonemes to viseme text files
    def map_phonemes_to_visemes(self, phonemes):
        viseme_mapping = {
            '-': 'closed.txt',
            'M': 'closed.txt',
            'P': 'closed.txt',
            'B': 'closed.txt',
            'F': 'teeth.txt',
            'V': 'teeth.txt',
            'T': 'sopen.txt',
            'D': 'sopen.txt',
            'E': 'sopen.txt',
            'L': 'sopen.txt',
            'S': 'wide.txt',
            'Z': 'wide.txt',
            'Ch': 'wide.txt',
            'J': 'wide.txt',
            'A': 'open.txt',
            'I': 'open.txt',
            'U': 'open.txt',
            'O': 'open.txt',

            
            # Add more mappings as needed
        }
 
        
    