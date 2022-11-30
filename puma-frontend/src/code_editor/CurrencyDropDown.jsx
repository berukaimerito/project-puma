import React from 'react'
import Select from 'react-select'
import { styles as customStyles } from '../constants/styles'
import { currencies } from '../constants/currencies'

const CurrencyDropDown = ({ handleCurrencyChange }) => {
  return (
    <Select
      placeholder={`Select Currency`}
      options={currencies}
      styles={customStyles}
      defaultValue={currencies[0]}
      onChange={(selectedOption) => handleCurrencyChange(selectedOption)}
    />
  )
}

export default CurrencyDropDown
