import React from 'react'
import Select from 'react-select'
import { styles as customStyles } from '../constants/styles'
import { languages as languageOptions } from '../constants/languages'

const LanguagesDropdown = ({ onSelectChange }) => {
  return (
    <Select
      placeholder={`Filter By Category`}
      options={languageOptions}
      styles={customStyles}
      defaultValue={languageOptions[0]}
      onChange={(selectedOption) => onSelectChange(selectedOption)}
    />
  )
}

export default LanguagesDropdown
