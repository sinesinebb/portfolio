/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class',
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['"JetBrains Mono"', 'ui-monospace', 'monospace'],
      },
      colors: {
        brand: {
          50: '#ecfdf7', 100: '#d1faec', 200: '#a7f3d9', 300: '#6ee7c0', 400: '#34d3a3',
          500: '#10b98a', 600: '#059670', 700: '#04775c', 800: '#065f4b', 900: '#064e3f',
        },
      },
    },
  },
}
