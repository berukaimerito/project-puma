import React, { useEffect, useState } from 'react'

import Editor from '@monaco-editor/react'

const CodeEditorWindow = ({ onChange, language, code, theme }) => {
  const [value, setValue] = useState(code || '')

  const handleEditorChange = (value) => {
    setValue(value)
    onChange('code', value)
  }

  useEffect(() => {
    setValue(code || '')
  }, [code])

  return (
    <div style={{ borderRadius: '25px', border: '5px' }}>
      <Editor
        height="85vh"
        width={`100%`}
        language={language || 'javascript'}
        value={value}
        theme={theme}
        defaultValue=""
        onChange={handleEditorChange}
      />
    </div>
  )
}
export default CodeEditorWindow
