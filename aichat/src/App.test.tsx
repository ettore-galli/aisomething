import { render, screen } from '@testing-library/react'
import { test, expect } from 'vitest'
import App from './App'

test('renders hello world', () => {
  render(<App />)
  expect(screen.getAllByText(/vite/i)[0]).toBeInTheDocument()
})