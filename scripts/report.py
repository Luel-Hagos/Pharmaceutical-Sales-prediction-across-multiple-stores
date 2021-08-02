with open('results.txt', 'w') as result:
      result.write('Linear Regression Pipeline wit k=5\n')
      result.write(f'r2 score: 0.5446401125789557 \nmean squared error: 0.4289427624982098\n')

      result.write('Random Forest Regressor with k=5\n')
      result.write(f'r2 score: 0.8964629232829608 \nmean squared error: 0.09753050484864338\n')
