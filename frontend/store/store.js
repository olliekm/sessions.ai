import { create } from 'zustand'

const useStore = create((set) => ({
  questions: {},
  setQuestions: (newQuestions) => set({ questions: newQuestions }),
  removeQuestion: (key) => set((state) => {
    const newQuestions = { ...state.questions }
    delete newQuestions[key]
    return { questions: newQuestions }
  }),
}))

export default useStore