import React, { useEffect, useState } from 'react'
import CodeEditorWindow from './CodeEditorWindow'
import axios from 'axios'
import { languages as languageOptions } from '../constants/languages'

import { ToastContainer, toast } from 'react-toastify'
import 'react-toastify/dist/ReactToastify.css'

import { defineTheme } from '../lib/defineTheme'
import useKeyPress from '../hooks/useKeyPress'
import OutputWindow from './OutputWindow'
import OutputDetails from './OutputDetails'
import ThemeDropdown from './ThemeDropdown'
import LanguagesDropdown from './LanguagesDropdown'
import { Button, Col, Row } from 'react-bootstrap'
import CurrencyDropDown from './CurrencyDropDown'
import { useNavigate, useParams } from 'react-router'
import scriptService from '../services/script.service'

const javascriptDefault = `/**
* Default code.
*/


const basicFunction = () => {
 return 2+2;
};
console.log(basicFunction());
`

const Landing = () => {
  const params = useParams()

  const [code, setCode] = useState(javascriptDefault)
  const [customInput, setCustomInput] = useState('')
  const [outputDetails, setOutputDetails] = useState(null)
  const [processing, setProcessing] = useState(null)
  const [theme, setTheme] = useState('cobalt')
  const [currency, setCurrency] = useState(params.id ? params.id : 'BTCUSDT')
  const [language, setLanguage] = useState(languageOptions[0])
  const navigate = useNavigate()


  const enterPress = useKeyPress('Enter')
  const ctrlPress = useKeyPress('Control')

  const onSelectChange = (sl) => {
    console.log('selected Option...', sl)
    setLanguage(sl)
  }

  useEffect(() => {
    if (enterPress && ctrlPress) {
      console.log('enterPress', enterPress)
      console.log('ctrlPress', ctrlPress)
    }
  }, [ctrlPress, enterPress])

  const onChange = (action, data) => {
    switch (action) {
      case 'code': {
        setCode(data)
        break
      }
      default: {
        console.warn('case not handled!', action, data)
      }
    }
  }
 
  function handleThemeChange(th) {
    const theme = th
    console.log('theme...', theme)

    if (['light', 'vs-dark'].includes(theme.value)) {
      setTheme(theme)
    } else {
      defineTheme(theme.value).then((_) => setTheme(theme))
    }
  }

  function handleCurrencyChange(crr) {
    setCurrency(crr.value)
  }

  useEffect(() => {
    defineTheme('oceanic-next').then((_) =>
      setTheme({ value: 'oceanic-next', label: 'Oceanic Next' })
    )
  }, [])

  useEffect(() => {
    if (params.id) {
      console.log('test11111')
      scriptService.getScriptById(params.id).then((data)=> {
        console.log(data)
        setCode(data[0].code)
      })
     
    }
    console.log(code)
  }, [])

  const saveCode = () => {
    scriptService.saveScript(code, currency).then((data)=> {
      console.log(data)
      navigate("/dashboard")
   })
  }

  const editCode = () => {
    scriptService.editScript(currency, code).then((data)=> {
      console.log(data)
      navigate("/dashboard")
   })
  }

  const handleRun = () => {
    scriptService.runScript(currency).then((data)=> {
      console.log(data)
      navigate("/dashboard")
   })
  }

  const handleStop = () => {
    scriptService.stopScript(currency).then((data)=> {
      console.log(data)
      navigate("/dashboard")
   })
  }

  const showSuccessToast = (msg) => {
    toast.success(msg || `Compiled Successfully!`, {
      position: 'top-right',
      autoClose: 1000,
      hideProgressBar: false,
      closeOnClick: true,
      pauseOnHover: true,
      draggable: true,
      progress: undefined,
    })
  }
  const showErrorToast = (msg, timer) => {
    toast.error(msg || `Something went wrong! Please try again.`, {
      position: 'top-right',
      autoClose: timer ? timer : 1000,
      hideProgressBar: false,
      closeOnClick: true,
      pauseOnHover: true,
      draggable: true,
      progress: undefined,
    })
  }
  console.log(currency)
  return (
    <>
      <ToastContainer
        position="top-right"
        autoClose={2000}
        hideProgressBar={false}
        newestOnTop={false}
        closeOnClick
        rtl={false}
        pauseOnFocusLoss
        draggable
        pauseOnHover
      />

      <Row className="justify-content-md-start">
        <Col sm={2} className="px-4 py-2">
          <LanguagesDropdown onSelectChange={onSelectChange} />
        </Col>
        <Col sm={2} className="px-4 py-2">
          <ThemeDropdown handleThemeChange={handleThemeChange} theme={theme} />
        </Col>
        <Col sm={2} className="px-4 py-2">
          <CurrencyDropDown handleCurrencyChange={handleCurrencyChange} currencyId={params.id ? params.id : ""} theme={theme} />
        </Col>
      </Row>
      <Row>
        <Col sm={8}>
          <CodeEditorWindow
            code={code}
            onChange={onChange}
            language={language?.value}
            theme={theme.value}
          />
        </Col>

        <Col sm={4}>
          <OutputWindow outputDetails={outputDetails} />
          <div className="flex flex-col items-end">
            <button style={{ color: 'green' }} onClick={handleRun} disabled={!code}>
              {processing ? 'Processing...' : 'Run'}
            </button>
            <button style={{ marginLeft: '10px', color: 'red' }} onClick={handleStop}>{'Stop'}</button>
          </div>
          {outputDetails && <OutputDetails outputDetails={outputDetails} />}
          <div style={{ marginTop: '10px' }}>
            <Button size="lg" variant="success" onClick={params.id ? editCode : saveCode}>
              {params.id ? 'Save Changes' : 'Save Script'}
            </Button>
          </div>
        </Col>
      </Row>
    </>
  )
}
export default Landing
