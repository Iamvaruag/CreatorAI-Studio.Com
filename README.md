# CreatorAI Studio🎨

CreatorAI Studio is an all-in-one, next-generation creative suite powered by artificial intelligence. Designed for content creators, digital artists, marketers, and developers, it streamlines the entire content lifecycle—from ideation and asset generation to editing and publishing.

✨ Key Features

✍️ AI Copy & Script Writer: Generate engaging blog posts, video scripts, social media captions, and marketing copy tailored to your brand's voice.

🖼️ Text-to-Image & Asset Studio: Create high-resolution illustrations, thumbnails, and concept art with fine-grained control over style, lighting, and aspect ratio.

🎙️ Voice & Audio Synthesis: Realistic text-to-speech voiceovers, podcast enhancement, and royalty-free background music generation.

🎬 Smart Video Workflows: Automated B-roll suggestions, dynamic captioning, and scene-by-scene storyboarding.

🗂️ Unified Workspace: Organize projects, manage brand kits (fonts, color palettes, tone guidelines), and collaborate with your team in real time.

🛠️ Tech Stack

Frontend: React / Next.js, TypeScript, Tailwind CSS

Backend: Node.js / Python (FastAPI)

AI & ML Integration: OpenAI API, Stability AI, ElevenLabs, Hugging Face

Database & Storage: PostgreSQL, Redis, AWS S3 / Cloudflare R2

Authentication: NextAuth.js / Clerk

🚀 Getting Started

Follow these instructions to set up a local development environment.

Prerequisites

Node.js (v18.0 or higher)

Python (v3.10 or higher, if running local inference workers)

npm, yarn, or pnpm

Git

Installation

Clone the repository:

git clone https://github.com/yourusername/creatorai-studio.git
cd creatorai-studio


Install dependencies:

npm install


Configure environment variables:
Copy the example environment file and populate it with your API keys and database credentials.

cp .env.example .env.local


Set up the database:

npx prisma migrate dev


Start the development server:

npm run dev


Open [http://localhost:3000](http://localhost:3000) in your browser to launch the studio.


🔐 Environment Variables

To run this project, you will need to add the following variables to your .env.local file:

# App Configuration
NEXT_PUBLIC_APP_URL=http://localhost:3000

# Database
DATABASE_URL="postgresql://user:password@localhost:5432/creatorai"

# AI Provider Keys
OPENAI_API_KEY="sk-..."
STABILITY_API_KEY="sk-..."
ELEVENLABS_API_KEY="..."

# Storage (S3 / R2)
STORAGE_BUCKET_NAME="creatorai-assets"
STORAGE_ACCESS_KEY="..."
STORAGE_SECRET_KEY="..."


📁 Project Structure

creatorai-studio/
├── public/                 # Static assets and icons
├── src/
│   ├── app/                # Next.js App Router pages and API routes
│   ├── components/         # Reusable UI and studio canvas components
│   ├── lib/                # AI SDK wrappers, utilities, and helpers
│   ├── store/              # Global state management (Zustand/Redux)
│   └── types/              # TypeScript interfaces and definitions
├── prisma/                 # Database schema and migrations
├── .env.example            # Template for environment variables
└── package.json            # Project dependencies and scripts


🗺️ Roadmap

[x] Multi-modal prompt builder (Text & Image)

[x] Project folders and asset history

[ ] Real-time multiplayer canvas collaboration

[ ] Custom fine-tuned LoRA model uploads

[ ] Direct publishing integrations (YouTube, TikTok, WordPress)

🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License

Distributed under the MIT License. See LICENSE for more information.

💬 Contact & Support

Have questions, feedback, or feature requests?

Open an issue in this repository.

Join our community Discord: discord.gg/creatorai

Email us at: support@creatorai.studio
