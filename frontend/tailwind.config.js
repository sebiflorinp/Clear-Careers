/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily:{
        'montserrat': ["Montserrat"],
        'tinos': ["Tinos"],
      },
      backgroundImage: {
        'main-page': "url('/src/assets/main-page-bg.webp')",
        backgroundOpacity:{'75': '.75'}
      }
    },
  },
  plugins: [],
}